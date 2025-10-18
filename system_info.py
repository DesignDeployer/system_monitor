# ---------- Monitoring Application ----------
# This file contains functions dedicated to retrieving system resource information
# using the 'psutil' library.
# Import the psutil library, which provides an interface for retrieving information
# on running processes and system utilization (CPU, memory, disks, network, sensors).

import psutil

def get_cpu_usage():
    """
    Retrieves the current system-wide CPU utilization as a percentage.
    Uses psutil.cpu_percent with interval=1 for a more stable reading over 1 second.
    """
# psutil.cpu_percent calculates the CPU usage percentage.
# interval=1 is crucial: it measures usage over a 1-second period, preventing inaccurate readings.

    return psutil.cpu_percent(interval=1) 

def get_memory_usage():

# Get detailed memory statistics object from psutil.
    memory_info = psutil.virtual_memory()

# 1 GB = 1024 * 1024 * 1024 bytes (1024**3). Round to 2 decimal places for readability.
    total_gb = round(memory_info.total / (1024**3), 2)
    used_gb = round(memory_info.used / (1024**3), 2)
    percent_used = memory_info.percent
    return percent_used, used_gb, total_gb

def get_disk_usage():

# Get disk usage statistics for the root filesystem ('/').
# On Windows, '/' typically maps to the C: drive.
    disk_info = psutil.disk_usage('/')
    total_gb = round(disk_info.total / (1024**3), 2)
    used_gb = round(disk_info.used / (1024**3), 2)
    percent_used = disk_info.percent
    return percent_used, used_gb, total_gb
