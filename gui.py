# ---------- Systemutveckling i Python ----------
# This file contains the GUI implementation for the monitoring application.
# It uses tkinter to create a simple interface displaying system stats.

import tkinter as tk
from system_info import get_cpu_usage, get_memory_usage, get_disk_usage

class App:
    def __init__(self, root, alarms_list):
        self.root = root
        self.alarms_list = alarms_list
        self.root.title("System Monitor")
    
        self.cpu_var = tk.StringVar(value="CPU: ...")
        self.memory_var = tk.StringVar(value="Memory: ...")
        self.disk_var = tk.StringVar(value="Disk: ...")
    
        self.cpu_label = tk.Label(self.root, textvariable=self.cpu_var, font=("Helvetica", 14))
        self.memory_label = tk.Label(self.root, textvariable=self.memory_var, font=("Helvetica", 14))
        self.disk_label = tk.Label(self.root, textvariable=self.disk_var, font=("Helvetica", 14))

        # TODO: Add alarm indicators

        self.cpu_label.pack(pady=10)
        self.memory_label.pack(pady=10)
        self.disk_label.pack(pady=10)
    
        self.update_stats()
    
    def update_stats(self):
        cpu_usage = get_cpu_usage()
        mem_usage, _, _ = get_memory_usage()
        disk_usage, _, _ = get_disk_usage()

        self.cpu_var.set(f"CPU Usage: {cpu_usage}%")
        self.memory_var.set(f"Memory Usage: {mem_usage}%")
        self.disk_var.set(f"Disk Usage: {disk_usage}%")

        self.root.after(1000, self.update_stats)