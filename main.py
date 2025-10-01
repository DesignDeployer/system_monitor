# ---------- Systemutveckling i Python ----------
# This is the main file for our monitoring application:

from system_info import get_cpu_usage, get_memory_usage, get_disk_usage

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
            print("\n--- Active Monitoring Status ---")
            
            cpu_percent = get_cpu_usage()
            print(f"CPU Usage: {cpu_percent}%")
            
            memory_percent, memory_used_gb, memory_total_gb = get_memory_usage()
            print(f"Memory Usage: {memory_percent}% ({memory_used_gb} GB out of {memory_total_gb} GB used)")
            
            disk_percent, disk_used_gb, disk_total_gb = get_disk_usage()
            print(f"Disk Usage: {disk_percent}% ({disk_used_gb} GB out of {disk_total_gb} GB used)")
            
            input("\nPress Enter to return to the menu...")
            
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