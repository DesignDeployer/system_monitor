# ---------- Systemutveckling i Python ----------
# Contains functions for saving and loading data to/from files.

import json
import os
from alarm import Alarm

ALARMS_FILE = "alarms.json"

def save_alarms(alarms_list):
    '''Converts a list of Alarm object to JSON and saves them to a file.'''
    data_to_save = [alarm.__dict__ for alarm in alarms_list]

    try:
        with open(ALARMS_FILE, 'w') as file:
            json.dump(data_to_save, file, indent=4)
        return True
    except IOError as e:
        print(f"Error saving alarms to file: {e}")
        return False
    
def load_alarms():
    '''Loads alarms from a JSON file and converts them to a list of Alarm objects.'''
    if not os.path.exists(ALARMS_FILE):
        return []

    try:
        with open(ALARMS_FILE, 'r') as file:
            data_from_file = json.load(file)
            loaded_alarms = []
            for alarm_data in data_from_file:
                alarm = Alarm(alarm_type=alarm_data['alarm_type'], threshold=alarm_data['threshold'])
                loaded_alarms.append(alarm)

            return loaded_alarms
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading alarms from file: {e}")
        return []