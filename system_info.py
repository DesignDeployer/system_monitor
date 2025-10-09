# ---------- Systemutveckling i Python ----------
# This file contains functions to retrieve system information.

import psutil

def get_cpu_usage():
    """
    cpu_percent är min verktyg som hämtas av psutil och "interval=1" då mätter jag användningen under 1 sekund för att få ett mer stabilt och korrekt värde.
    """
    return psutil.cpu_percent(interval=1) 

def get_memory_usage():
    memory_info = psutil.virtual_memory()
    total_gb = round(memory_info.total / (1024**3), 2)
    used_gb = round(memory_info.used / (1024**3), 2)
    percent_used = memory_info.percent
    return percent_used, used_gb, total_gb

def get_disk_usage():
    disk_info = psutil.disk_usage('/')
    total_gb = round(disk_info.total / (1024**3), 2)
    used_gb = round(disk_info.used / (1024**3), 2)
    percent_used = disk_info.percent
    return percent_used, used_gb, total_gb
