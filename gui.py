# ---------- Monitoring Application ----------
# This file contains the GUI implementation for the monitoring application.
# It uses tkinter to create a simple interface displaying system stats.

import tkinter as tk    # Import tkinter, aliased as 'tk' for brevity.
from system_info import get_cpu_usage, get_memory_usage, get_disk_usage

class App:
    def __init__(self, root, alarms_list):
        self.root = root
        self.alarms_list = alarms_list
        self.root.title("System Monitor")

# --- Tkinter Variables for Dynamic Labels ---
# via 'textvariable' will automatically update its displayed text.
        self.cpu_var = tk.StringVar(value="CPU: ...")
        self.memory_var = tk.StringVar(value="Memory: ...")
        self.disk_var = tk.StringVar(value="Disk: ...")

# --- Create GUI Widgets (Labels) ---
# Create Label widgets to display the text.
# - The first argument ('self.root') specifies the parent window for the label.
# - 'textvariable' links the label's text content to the corresponding StringVar.
# - 'font' sets the text appearance.
        self.cpu_label = tk.Label(self.root, textvariable=self.cpu_var, font=("Helvetica", 14))
        self.memory_label = tk.Label(self.root, textvariable=self.memory_var, font=("Helvetica", 14))
        self.disk_label = tk.Label(self.root, textvariable=self.disk_var, font=("Helvetica", 14))

        # TODO: Add alarm indicators

# --- Place Widgets onto the Window ---
# Use the 'pack' geometry manager to place the labels in the window.
# 'pack' simply stacks widgets vertically (by default) in the available space.
# 'pady' adds some vertical padding (space) around each label.
        self.cpu_label.pack(pady=10)
        self.memory_label.pack(pady=10)
        self.disk_label.pack(pady=10)
    
        self.update_stats()
    
    def update_stats(self):
        cpu_usage = get_cpu_usage()
# Use '_' to ignore the unused GB values returned by the functions.
        mem_usage, _, _ = get_memory_usage()
        disk_usage, _, _ = get_disk_usage()

        self.cpu_var.set(f"CPU Usage: {cpu_usage}%")
        self.memory_var.set(f"Memory Usage: {mem_usage}%")
        self.disk_var.set(f"Disk Usage: {disk_usage}%")

# --- Schedule the next update ---
# Use tkinter's 'after' method to schedule this *same* function ('self.update_stats')
# to be called again after a specified delay (in milliseconds).
# This creates a non-blocking loop that keeps the GUI responsive while updating data.
# 1000ms = 1 second.
# IMPORTANT: Never use time.sleep() in the main thread of a tkinter app, as it freezes the GUI.
        self.root.after(1000, self.update_stats)