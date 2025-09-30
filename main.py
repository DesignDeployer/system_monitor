# ---------- Systemutveckling i Python ----------
# This is the main file for our monitoring application:

def main_menu():

    while True:
        print("\n--- Main Menu ---")
        print("1. Start Monitoring")
        print("2. List Active Monitoring")
        print("3. Create Alarm")
        print("4. View Alarms")
        print("5. Enter Monitoring Mode")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            print("You selected: Start Monitoring (Functionality to be added later)")
            pass
        elif choice == '2':
            print("You selected_ List Active Monitoring (Functionality to be added later)")
            pass
        elif choice == '3':
            print("You selected: Create Alarm (Functionality to be added later)")
            pass
        elif choice == '4':
            print("You Selected: View Alarms (Functionality to be added later)")
            pass
        elif choice == '5':
            print("You Selected: Enter Monitoring Mode (Functionality to be added later)")
            pass
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()