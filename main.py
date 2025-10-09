# ---------- Systemutveckling i Python ----------
# This is the main file for our monitoring application.

from system_info import get_cpu_usage, get_memory_usage, get_disk_usage
from alarm import Alarm
import time
import msvcrt
import logging
from logger_config import setup_logging
from file_handler import save_alarms, load_alarms

def monitoring_mode(alarms_list):
    """
    Enters an active monitoring loop that checks stats against alarms.
    """
    print("\n--- Entering Monitoring Mode ---")
    print("Monitoring is active. Press any key to return to the menu.")
    
    logging.info("Monitoring_Mode_Started")

    while True:
        if msvcrt.kbhit():
            print("\nKey pressed, exiting monitoring mode...")
            logging.info("Monitoring_Mode_Exited_by_user")
            msvcrt.getch() 
            break

        current_cpu = get_cpu_usage()
        current_mem_percent, _, _ = get_memory_usage()
        current_disk_percent, _, _ = get_disk_usage()

        for alarm in alarms_list:
            if alarm.alarm_type == "CPU" and current_cpu > alarm.threshold:
                print(f"\n*** WARNING, ALARM TRIGGERED: CPU USAGE EXCEEDS {alarm.threshold}% ***")
                logging.warning(f"CPU_Alarm_Triggered_Threshold_{alarm.threshold}%_Current_{current_cpu}%")

            elif alarm.alarm_type == "Memory" and current_mem_percent > alarm.threshold:
                print(f"\n*** WARNING, ALARM TRIGGERED: MEMORY USAGE EXCEEDS {alarm.threshold}% ***")
                logging.warning(f"Memory_Alarm_Triggered_Threshold_{alarm.threshold}%_Current_{current_mem_percent}%")
                
            elif alarm.alarm_type == "Disk" and current_disk_percent > alarm.threshold:
                print(f"\n*** WARNING, ALARM TRIGGERED: DISK USAGE EXCEEDS {alarm.threshold}% ***")
                logging.warning(f"Disk_Alarm_Triggered_Threshold_{alarm.threshold}%_Current_{current_disk_percent}%")

        print(f"Monitoring... Last check: CPU {current_cpu}%, Mem {current_mem_percent}%, Disk {current_disk_percent}%. Press any key to exit.", end="\r")
        
        time.sleep(5)

def view_alarms(alarms_list):
    """Displays all configured alarms, sorted by type."""
    logging.info("User_selected_View_Alarms")

    print("\n--- Configured Alarms ---")

    if not alarms_list:
        print("No alarms have been configured yet.")

    else:
        sorted_alarms = sorted(alarms_list, key=lambda alarm: alarm.alarm_type)
        for index, alarm in enumerate(sorted_alarms, start=1):
            print(f"{index}. {alarm.alarm_type} alarm {alarm.threshold}%")
    input("\nPress Enter to return to the menu...")

def create_alarm_menu(alarms_list):
    """Handles the alarm creation process."""
    logging.info("User_selected_Create_Alarm")

    while True:
        if type_choice in alarm_type_map:
            alarm_type = alarm_type_map[type_choice]
            logging.info(f"User_is_configuring_{alarm_type}_alarm")
            while True:
                threshold_input = input(f"Set alarm threshold for {alarm_type} Usage (1-100): ")
                if threshold_input.isdigit():
                    threshold = int(threshold_input)
                    if 1 <= threshold <= 100:
                        new_alarm = Alarm(alarm_type=alarm_type, threshold=threshold)
                        alarms_list.append(new_alarm)
                        save_alarms(alarms_list)
                        print(f"Success: Alarm for {alarm_type} Usage set to {threshold}%.")
                        logging.info(f"{alarm_type}_Alarm_Created_Threshold_{threshold}%")
                        return
    return

def create_alarm_menu(alarms_list):
    """Handles the alarm creation process."""
    logging.info("User_selected_Create_Alarm")

    while True:
        print("\n--- Configure Alarm ---")
        print("1. CPU Usage")
        print("2. Memory Usage")
        print("3. Disk Usage")
        print("4. Back to Main Menu")
        type_choice = input("Select alarm type (1-4): ")
        alarm_type_map = {"1": "CPU", "2": "Memory", "3": "Disk"}
        if type_choice in alarm_type_map:
            alarm_type = alarm_type_map[type_choice]
            logging.info(f"User_is_configuring_{alarm_type}_alarm")
            while True:
                threshold_input = input(f"Set alarm threshold for {alarm_type} Usage (1-100): ")
                if threshold_input.isdigit():
                    threshold = int(threshold_input)
                    if 1 <= threshold <= 100:
                        new_alarm = Alarm(alarm_type=alarm_type, threshold=threshold)
                        alarms_list.append(new_alarm)
                        print(f"Success: Alarm for {alarm_type} Usage set to {threshold}%.")
                        logging.info(f"{alarm_type}_Alarm_Created_Threshold_{threshold}%")
                        return
                    else:
                        print("Error: Please enter a number between 1 and 100.")
                else:
                    print("Error: Invalid input. Please enter a number.")
        elif type_choice == '4':
            logging.info("User_returned_to_main_menu_from_alarm_config")
            return
        else:
            print("Invalid choice. Please select 1-4.")

def main_menu():
    """Displays the main menu and handles user input."""
    monitoring_active = False
    alarms = load_alarms()
    logging.info(f"Loaded_{len(alarms)}_alarms_from_file")
    print("Loading previously configured alarms...")
    
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
            logging.info("User_selected_Start_Monitoring")
            print("\nMonitoring has been started.")
            input("Press Enter to continue...")

        elif choice == '2':
            logging.info("User_selected_List_Active_Monitoring")
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
            view_alarms(alarms)
        elif choice == '5':
            monitoring_mode(alarms)
        elif choice == '6':
            logging.info("User_selected_Exit. Program_shutting_down.")
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    setup_logging()
    logging.info("Application_Started")
    main_menu()