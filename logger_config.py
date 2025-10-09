# ---------- Systemutveckling i Python ----------
# This file contains the configuration for the application's logger.

import logging
import datetime

def setup_logging():
    '''Sets up a new log file for each run with a dynamic filename.'''
    log_filename = datetime.datetime.now().strftime("monitor_log_%Y_%m_%d_%H_%M_%S.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s_%(message)s",
        datefmt="%Y-%m-%d_%H:%M:%S",
        filename=log_filename,
        filemode='w'
    )