from devices.smart_light import SmartLight


# Initialize devices
smart_light = SmartLight()


def show_menu():
    print("\nIoT Device Monitor")
    print("1. Toggle Smart Light")
  
    print("4. Exit")

def execute_action(choice):
    if choice == 1:
        smart_light.toggle()
    elif choice == 2:
        temperature = float(input("Enter temperature (°C): "))
        thermostat.set_temperature(temperature)
    elif choice == 3:
        security_camera.detect_motion()
    elif choice == 4:
        print("Exiting program.")
        exit(0)
    else:
        print("Invalid choice! Please try again.")

def main():
    while True:
        show_menu()
        try:
            choice = int(input("Select an action: "))
            execute_action(choice)
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
