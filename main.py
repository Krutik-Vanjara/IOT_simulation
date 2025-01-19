from thermostat import Thermostat

# Menu functions
def show_menu():
    print("\nMain Menu:")
    print("1. Manage Smart Lights")
    print("2. Manage Thermostat")
    print("3. View Logs")
    print("4. Exit")

def smart_light_menu():
    print("\nSmart Light Menu:")
    print("1. Turn ON/OFF")
    print("2. Adjust Brightness")
    print("3. Back to Main Menu")

def thermostat_menu():
    print("\nThermostat Menu:")
    print("1. Turn ON/OFF")
    print("2. Set Temperature")
    print("3. Back to Main Menu")

# Main program
def main():
    thermostat = Thermostat()

    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            smart_light_menu()
            # Add logic for smart light actions
        elif choice == "2":
            while True:
                thermostat_menu()
                t_choice = input("Enter your choice for Thermostat: ")
                
                if t_choice == "1":
                    thermostat.toggle_status()
                elif t_choice == "2":
                    try:
                        target_temp = int(input("Enter the target temperature (16-30°C): "))
                        thermostat.set_temperature(target_temp)
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif t_choice == "3":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Viewing Logs... (This feature will be implemented soon!)")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()
