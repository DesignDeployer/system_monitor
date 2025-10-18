# ---------- Monitoring Application ----------
# This file contains the setup function for the application's logging configuration.

import logging  # Python's standard logging library.
import datetime  # Used to get the current timestamp for the log filename.

def setup_logging():
    '''
    Configures the logging system to write to a unique file for each application run.
    '''

# strftime formats the datetime object into a string like 'monitor_log_2025-10-17_21-45-30.log'.
    log_filename = datetime.datetime.now().strftime("monitor_log_%Y_%m_%d_%H_%M_%S.log")

# --- Configure the root logger ---
# basicConfig is a one-time setup for the logging system.
    logging.basicConfig(

# Set the minimum severity level to log. INFO means INFO, WARNING, ERROR, CRITICAL messages will be logged.
        level=logging.INFO,

# Define the format for each log entry.
# %(asctime)s: Adds the timestamp of the log record.
# %(message)s: Adds the actual log message passed to logging.info(), etc.
# The underscore '_' is used as a separator.
        format="%(asctime)s_%(message)s",
        datefmt="%Y-%m-%d_%H:%M:%S",
        filename=log_filename,
        filemode='w'
    )