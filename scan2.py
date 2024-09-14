import time
from pyrplidar import PyRPlidar
from globali import angle, distance 
from plotPolar import plot_lidar_data, plot_lidar_live
import threading


rp_cfg = {
    'port': '/dev/cu.usbserial-1440',
    'baudrate': 460800,
    'timeout': 3,
}

stop_event = threading.Event()

def simple_scan(rp_cfg, stop_event):
    LiDAR = PyRPlidar()
    LiDAR.connect(**rp_cfg)
    angle.clear()
    distance.clear()
    try:
        samplerate = LiDAR.get_samplerate()
        LiDAR.set_motor_pwm(samplerate.t_standard)
        time.sleep(2)
        scan_generator = LiDAR.start_scan()
        for _, scan in enumerate(scan_generator()):
            if scan.quality > 0:
                angle.append(scan.angle)
                distance.append(scan.distance)
            if stop_event.is_set():
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        LiDAR.stop()
        LiDAR.set_motor_pwm(0)
        LiDAR.disconnect()

if __name__ == "__main__":
    try:
        # Create and start the scanning thread
        t1 = threading.Thread(target=simple_scan, args=(rp_cfg, stop_event), daemon=True)
        t1.start()
        plot_lidar_live()
    except KeyboardInterrupt:
        # Set the stop event and wait for the thread to finish
        print("Stopping LiDAR scan...")
        stop_event.set()
        t1.join()
    finally:
        print("LiDAR scan stopped.")

