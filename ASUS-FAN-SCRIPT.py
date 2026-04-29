import os
import sys
import time

if os.geteuid() != 0:
    print("Run via: sudo python3 ASUS-FAN-SCRIPT.py")
    sys.exit()

def main():
    while True:
        os.system('clear')
        print("---ASUS-FAN-SCRIPT---")
        print("1. TURBO (100% speed)")
        print("2. BASE")
        print("3. EXIT")
        
        choice = input("\n> ")

        if choice == '1':
            print("\n[TURBO]")
            os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")
            os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*_enable")
            os.system("echo 255 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*")
            time.sleep(3)
            
        elif choice == '2':
            print("\n[BASE]")
            os.system("echo 0 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")
            os.system("echo 2 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*_enable")
            time.sleep(3)
            
        elif choice == '3':
            print("Exit...")
            break

if __name__ == "__main__":
    main()
