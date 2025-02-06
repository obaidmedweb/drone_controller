from pymavlink import mavutil
import time
import math

class DroneController:
    def __init__(self, connection_string='udp:127.0.0.1:14550'):
        """
        Initialize drone controller
        :param connection_string: Connection string for the drone (simulator or real drone)
        """
        self.connection_string = connection_string
        self.vehicle = None
        self.armed = False
        self.target_system = 1
        self.target_component = 1

    def connect(self):
        """Connect to the drone"""
        print('Connecting to drone...')
        self.vehicle = mavutil.mavlink_connection(self.connection_string)
        self.vehicle.wait_heartbeat()
        print('Connected!')

    def arm_and_takeoff(self, target_altitude):
        """
        Arms the drone and takes off to target altitude
        :param target_altitude: Target altitude in meters
        """
        print('Basic pre-arm checks...')
        self.vehicle.mav.command_long_send(
            self.target_system,
            self.target_component,
            mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            0,
            1, 0, 0, 0, 0, 0, 0
        )

        # Wait for arming
        print('Waiting for arming...')
        while True:
            msg = self.vehicle.recv_match(type='HEARTBEAT', blocking=True)
            if msg.base_mode & mavutil.mavlink.MAV_MODE_FLAG_SAFETY_ARMED:
                print('Armed!')
                break

        # Take off
        print('Taking off!')
        self.vehicle.mav.command_long_send(
            self.target_system,
            self.target_component,
            mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            0,
            0, 0, 0, 0, 0, 0, target_altitude
        )

        # Monitor altitude
        while True:
            msg = self.vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
            current_altitude = msg.relative_alt / 1000.0  # Convert mm to meters
            print(f'Altitude: {current_altitude}m')
            if current_altitude >= target_altitude * 0.95:
                print('Reached target altitude')
                break
            time.sleep(1)

    def land(self):
        """Land the drone"""
        print('Landing...')
        self.vehicle.mav.command_long_send(
            self.target_system,
            self.target_component,
            mavutil.mavlink.MAV_CMD_NAV_LAND,
            0,
            0, 0, 0, 0, 0, 0, 0
        )
        
        # Monitor landing
        while True:
            msg = self.vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
            current_altitude = msg.relative_alt / 1000.0
            if current_altitude <= 0.1:
                print('Landing complete')
                break
            time.sleep(1)

    def goto_position(self, lat, lon, alt):
        """
        Go to specified position
        :param lat: Latitude
        :param lon: Longitude
        :param alt: Altitude in meters
        """
        self.vehicle.mav.mission_item_send(
            self.target_system,
            self.target_component,
            0,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,
            mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,
            2, 0, 0, 0, 0, 0,
            lat, lon, alt
        )
        
    def get_battery_status(self):
        """Get drone battery status"""
        msg = self.vehicle.recv_match(type='SYS_STATUS', blocking=True)
        return {
            'voltage': msg.voltage_battery / 1000.0,  # Convert mV to V
            'current': msg.current_battery / 100.0,   # Convert cA to A
            'remaining': msg.battery_remaining
        }

    def get_location(self):
        """Get current drone location"""
        msg = self.vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking=True)
        return {
            'lat': msg.lat / 1e7,  # Convert to degrees
            'lon': msg.lon / 1e7,  # Convert to degrees
            'alt': msg.relative_alt / 1000.0  # Convert mm to meters
        }

    def disconnect(self):
        """Disconnect from drone"""
        if self.vehicle:
            self.vehicle.close()
            print('Disconnected from drone')
