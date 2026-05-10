import os
import sys
import time

if os.geteuid() != 0:
    print("Run via: sudo python3 ASUS-FAN-SCRIPT.py")
    sys.exit()

def main():
    while True:
        os.system('clear')

        print("                  _____ _    _  _____       ______      _   _        _____  _____ _____  _____ _____ _______   ")  
        print("           /\    / ____| |  | |/ ____|     |  ____/\   | \ | |      / ____|/ ____|  __ \|_   _|  __ \__   __|  ")
        print("          /  \  | (___ | |  | | (___ ______| |__ /  \  |  \| |_____| (___ | |    | |__) | | | | |__) | | |     ")
        print("         / /\ \  \___ \| |  | |\___ \______|  __/ /\ \ | . ` |______\___ \| |    |  _  /  | | |  ___/  | |     ")
        print("        / ____ \ ____) | |__| |____) |     | | / ____ \| |\  |      ____) | |____| | \ \ _| |_| |      | |     ")
        print("       /_/    \_\_____/ \____/|_____/      |_|/_/    \_\_| \_|     |_____/ \_____|_|  \_\_____|_|      |_|     ")
        print("                                                                                                               ")
        print("                                                                                                               ")
        print("                                           [1] TURBO (100% speed)")
        print("                                           [2] MEDIUM (50% speed)")
        print("                                           [3] LOW (35% speed)")
        print("                                                 [4] BASE")
        print("                                                 [5] EXIT")
        
        choice = input("\n> ")

        if choice == '1':
            print("\n[TURBO - FIXED]")
            os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")
            os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*_enable")
            os.system("echo 255 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*")
            time.sleep(3)
            
        elif choice == '2':
            print("\n[MEDIUM - FIXED]")
            os.system("echo 0 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")
            os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*_enable")
            os.system("echo 128 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*")
            time.sleep(3)

        elif choice == '3':
            print("\n[LOW - FIXED]")
            os.system("echo 2 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")
            os.system("echo 1 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*_enable")
            os.system("echo 89 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*")
            time.sleep(3)

        elif choice == '4':
            print("\n[BASE - AUTO]")
            os.system("echo 0 | sudo tee /sys/devices/platform/asus-nb-wmi/throttle_thermal_policy")
            os.system("echo 2 | sudo tee /sys/devices/platform/asus-nb-wmi/hwmon/hwmon*/pwm*_enable")
            print("Control returned to System.")
            time.sleep(3)
            
        elif choice == '5':
            print("Exit...")
            break

if __name__ == "__main__":
    main()
