# مشروع برمجة الدرون 🚁
# Drone Programming Project

<div dir="rtl">

## الوصف
هذا المشروع يوفر واجهة برمجية متكاملة للتحكم في الطائرات بدون طيار (درون). يدعم المشروع مجموعة واسعة من الدرونات التي تستخدم بروتوكول MAVLink، بما في ذلك:
- DJI Drones
- Pixhawk
- ArduPilot
- PX4
- 3DR Solo
- وغيرها من الدرونات المتوافقة مع MAVLink

## المميزات
### 1. التحكم الأساسي
- الإقلاع التلقائي مع تحديد الارتفاع
- الهبوط الآمن والتلقائي
- التحكم في وضع الطيران (GUIDED, AUTO, RTL)
- التحكم في سرعة وتوجيه الدرون

### 2. الملاحة والموقع
- تحديد نقاط GPS للمسار
- التحرك إلى إحداثيات محددة
- تتبع المسار المبرمج مسبقاً
- العودة التلقائية إلى نقطة الانطلاق

### 3. المراقبة والتشخيص
- مراقبة مستوى البطارية
- عرض معلومات GPS في الوقت الحقيقي
- مراقبة الارتفاع والسرعة
- تشخيص حالة الاتصال

## المتطلبات التقنية
- Python 3.8 أو أحدث
- نظام تشغيل: Windows, macOS, أو Linux
- اتصال إنترنت (للتثبيت الأولي)

## التثبيت
1. تثبيت Python وأدوات التطوير:
```bash
# تثبيت pip إذا لم يكن موجوداً
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# إنشاء بيئة افتراضية
python3 -m venv .venv
source .venv/bin/activate  # على Linux/macOS
# أو
.venv\Scripts\activate  # على Windows
```

2. تثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

## كيفية الاستخدام

### 1. الاتصال بالدرون
```python
from drone_controller import DroneController

# للاتصال بمحاكي الدرون
drone = DroneController('udp:127.0.0.1:14550')

# للاتصال بالدرون عبر WiFi
# drone = DroneController('udp:192.168.4.1:14550')  # عنوان IP الافتراضي للدرون
# أو
# drone = DroneController('tcp:192.168.4.1:5760')    # بعض أنواع الدرون تستخدم TCP

# للاتصال بدرون حقيقي عبر USB
# drone = DroneController('/dev/ttyUSB0') # على Linux
# drone = DroneController('COM3')          # على Windows
# drone = DroneController('/dev/tty.usbserial-XXXXX') # على macOS

# ملاحظة: تأكد من الاتصال بشبكة WiFi الخاصة بالدرون أولاً
drone.connect()
```

### 2. الإقلاع والهبوط
```python
# الإقلاع إلى ارتفاع 10 أمتار
drone.arm_and_takeoff(10)

# الهبوط
drone.land()
```

### 3. التحرك إلى موقع محدد
```python
# الانتقال إلى إحداثيات محددة
drone.goto_position(latitude=24.9916, longitude=55.1741, altitude=20)
```

### 4. مراقبة حالة الدرون
```python
# معرفة مستوى البطارية
battery = drone.get_battery_status()
print(f"Battery: {battery['voltage']}V, {battery['remaining']}%")

# معرفة الموقع الحالي
location = drone.get_location()
print(f"Location: Lat={location['lat']}, Lon={location['lon']}, Alt={location['alt']}m")
```

## تنبيهات السلامة
1. تأكد دائماً من وجود مساحة كافية للطيران
2. تحقق من قوانين الطيران في منطقتك
3. تأكد من شحن البطارية قبل الطيران
4. قم دائماً باختبار البرنامج في المحاكي أولاً
5. احتفظ بوحدة تحكم يدوية للطوارئ

## حل المشكلات الشائعة
1. مشكلة الاتصال: تأكد من صحة منفذ الاتصال وسرعة نقل البيانات
2. خطأ في الإقلاع: تحقق من حالة GPS وقوة الإشارة
3. عدم الاستجابة للأوامر: تأكد من وضع الطيران (GUIDED mode)

</div>

## Description
This project provides a comprehensive programming interface for controlling drones. It supports a wide range of drones that use the MAVLink protocol, including:
- DJI Drones
- Pixhawk
- ArduPilot
- PX4
- 3DR Solo
- And other MAVLink-compatible drones

## Features
### 1. Basic Control
- Automatic takeoff with altitude specification
- Safe and automatic landing
- Flight mode control (GUIDED, AUTO, RTL)
- Drone speed and direction control

### 2. Navigation & Location
- Setting GPS waypoints
- Moving to specific coordinates
- Following pre-programmed paths
- Automatic return to launch point

### 3. Monitoring & Diagnostics
- Battery level monitoring
- Real-time GPS information
- Altitude and speed monitoring
- Connection status diagnostics

## Technical Requirements
- Python 3.8 or newer
- Operating System: Windows, macOS, or Linux
- Internet connection (for initial installation)

## Installation
1. Install Python and development tools:
```bash
# Install pip if not present
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # on Linux/macOS
# or
.venv\Scripts\activate  # on Windows
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

## How to Use

### 1. Connecting to the Drone
```python
from drone_controller import DroneController

# For connecting to drone simulator
drone = DroneController('udp:127.0.0.1:14550')

# For connecting to drone via WiFi
# drone = DroneController('udp:192.168.4.1:14550')  # Default drone IP address
# or
# drone = DroneController('tcp:192.168.4.1:5760')    # Some drones use TCP

# For connecting to real drone via USB
# drone = DroneController('/dev/ttyUSB0') # on Linux
# drone = DroneController('COM3')          # on Windows
# drone = DroneController('/dev/tty.usbserial-XXXXX') # on macOS

# Note: Make sure you're connected to the drone's WiFi network first
drone.connect()
```

### 2. Takeoff and Landing
```python
# Take off to 10 meters
drone.arm_and_takeoff(10)

# Land
drone.land()
```

### 3. Moving to a Location
```python
# Move to specific coordinates
drone.goto_position(latitude=24.9916, longitude=55.1741, altitude=20)
```

### 4. Monitoring Drone Status
```python
# Get battery status
battery = drone.get_battery_status()
print(f"Battery: {battery['voltage']}V, {battery['remaining']}%")

# Get current location
location = drone.get_location()
print(f"Location: Lat={location['lat']}, Lon={location['lon']}, Alt={location['alt']}m")
```

## Safety Warnings
1. Always ensure sufficient space for flying
2. Check local flight regulations
3. Verify battery charge before flight
4. Always test programs in simulator first
5. Keep a manual controller for emergencies

## Common Troubleshooting
1. Connection issues: Verify connection port and baud rate
2. Takeoff errors: Check GPS status and signal strength
3. Command unresponsiveness: Verify flight mode (GUIDED mode)

## License
MIT License

## Contributing
Contributions are welcome! Please read the contributing guidelines before submitting any changes.
