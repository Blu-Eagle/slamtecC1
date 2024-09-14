from pyrplidar import PyRPlidar
import time

lidar = PyRPlidar()
lidar.connect(port="/dev/cu.usbserial-1440", baudrate=460800, timeout=3)

def simple_scan():
    lidar.set_motor_pwm(200)
    time.sleep(2)

    scan_generator = lidar.start_scan()

    for count, scan in enumerate(scan_generator()):
        print(count, scan)
        if count == 20: break

    
    lidar.stop()
    lidar.set_motor_pwm(0)
    lidar.disconnect()

if __name__ == "__main__":
    simple_scan()