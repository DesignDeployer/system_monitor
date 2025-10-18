# ---------- Monitoring Application ----------
# This file defines the Alarm Class.

class Alarm:
    """
    Represents a single alarm with its type (e.g., 'CPU', 'Memory'), threshold value (percentage), and triggered state.
    """

# The constructor method, automatically called when a new Alarm object is created.
    def __init__(self, alarm_type, threshold):
        self.alarm_type = alarm_type
        self.threshold = threshold
        self.is_triggered = False