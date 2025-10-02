# ---------- Systemutveckling i Python ----------
# This is the main file for our monitoring application:

from system_info import get_cpu_usage, get_memory_usage, get_disk_usage
from alarm import Alarm

def create_alarm_menu(alarms_list):
    while True:
        print("\n--- Configure Alarm ---")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Back to Main Menu")

        type_choice = input("Select alarm type (1-4): ")
        
        alarm_type_map = {
            "1": "CPU",
            "2": "Memory",
            "3": "Disk"
        }

        if type_choice in alarm_type_map:
            alarm_type = alarm_type_map[type_choice]

            while True:
                threshold_input = input(f"Set alarm threshold for {alarm_type} Usage (1-100): ")
                if threshold_input.isdigit(): #".isdigit()" är en function för textsträngar som kollar "Består den här texten enbart av siffror?"
                    threshold = int(threshold_input)
                    if 1 <= threshold <= 100:
                        new_alarm = Alarm(alarm_type=alarm_type, threshold=threshold)
                        alarms_list.append(new_alarm)
                        print(f"Success: Alarm for {alarm_type} Usage set to {threshold}%.")
                        return
                    else:
                        print("Error: Please enter a number between 1 and 100.")
                else:
                    print("Error: Invalid input. Please enter a number.")
        elif type_choice == '4':
            return
        else:
            print("Invalid choice. Please select 1-4. ")


def main_menu():
    monitoring_active = False
    
    alarms = []

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
            monitoring_active = True
            print("\nMonitoring has been started.")
            input("press Enter to continue...")

        elif choice == '2':
            if monitoring_active:
                print("\n--- Active Monitoring Status ---")
            
                cpu_percent = get_cpu_usage()
                print(f"CPU Usage: {cpu_percent}%")
            
                memory_percent, memory_used_gb, memory_total_gb = get_memory_usage()
                print(f"Memory Usage: {memory_percent}% ({memory_used_gb} GB out of {memory_total_gb} GB used)")
            
                disk_percent, disk_used_gb, disk_total_gb = get_disk_usage()
                print(f"Disk Usage: {disk_percent}% ({disk_used_gb} GB out of {disk_total_gb} GB used)")
            
                input("\nPress Enter to return to the menu...")

            else:
                print("\nMonitoring is not active. Please start monitoring from the menu first.")
                input("Press Enter to continue...")
            
        elif choice == '3':
            create_alarm_menu(alarms)
            
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