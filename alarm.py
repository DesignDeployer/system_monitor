# ---------- Systemutveckling i Python ----------
# This file defines the Alarm Class.

class Alarm:
    """
    Represents a single alarm with its type and threshold. 
    """

    def __init__(self, alarm_type, threshold):
        self.alarm_type = alarm_type
        self.threshold = threshold