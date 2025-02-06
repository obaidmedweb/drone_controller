from drone_controller import DroneController
import time

def main():
    # Create drone controller instance
    # Use 'udp:127.0.0.1:14550' for simulator
    # For real drone, use appropriate connection string (e.g., '/dev/ttyUSB0' for USB)
    drone = DroneController()

    try:
        # Connect to the drone
        drone.connect()

        # Get initial battery status
        battery = drone.get_battery_status()
        print(f'Battery Status: {battery}')

        # Take off to 10 meters
        drone.arm_and_takeoff(10)

        # Hover for 5 seconds
        print('Hovering...')
        time.sleep(5)

        # Get current location
        location = drone.get_location()
        print(f'Current Location: {location}')

        # Move to a new position (adjust these coordinates based on your location)
        # These are example coordinates - replace with actual coordinates in your area
        drone.goto_position(location['lat'] + 0.0001, location['lon'] + 0.0001, 10)
        
        # Wait for movement to complete
        time.sleep(10)

        # Land the drone
        drone.land()

    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        # Always disconnect properly
        drone.disconnect()

if __name__ == '__main__':
    main()
