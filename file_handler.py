# ---------- Monitoring Application ----------
# This file contains utility functions for saving the list of Alarm objects
# to a persistent file (alarms.json) and loading them back when the app starts.

import json # For working with JSON data format (encoding/decoding).
import os   # Provides functions for interacting with the operating system, like checking if a file exists.
from alarm import Alarm

ALARMS_FILE = "alarms.json"

def save_alarms(alarms_list):
    '''
    Converts a list of Alarm object to JSON and saves them to a file.
    '''

# --- Prepare data for JSON serialization ---
# JSON cannot directly store custom Python objects (like our Alarm instances).
# It understands basic types: lists, dictionaries, strings, numbers, booleans, null.
# We convert each Alarm object into a dictionary using its '__dict__' attribute.
# '__dict__' conveniently holds the object's attributes (alarm_type, threshold, is_triggered) as key-value pairs.
# This list comprehension creates a new list containing these dictionaries.
    data_to_save = [alarm.__dict__ for alarm in alarms_list]

# --- Save the data to the file ---
# File operations can fail (e.g., disk full, permissions error), so use a try...except block.
    try:
        with open(ALARMS_FILE, 'w') as file:

# 'json.dump()' writes the Python data structure (our list of dicts) into the file
# in JSON text format.
# 'indent=4' makes the resulting JSON file human-readable with nice indentation.
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
# Create a new Alarm instance using the data from the dictionary.
# We access dictionary values using their keys ('alarm_type', 'threshold').
# NOTE: The 'is_triggered' state is *not* explicitly saved/loaded here,
# so it will default back to False based on the Alarm class __init__.
# If we wanted to preserve the triggered state, we'd need to add
# is_triggered=alarm_data.get('is_triggered', False) here and ensure it's saved.
                alarm = Alarm(alarm_type=alarm_data['alarm_type'], threshold=alarm_data['threshold'])
                loaded_alarms.append(alarm)

            return loaded_alarms
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading alarms from file: {e}")
        return []