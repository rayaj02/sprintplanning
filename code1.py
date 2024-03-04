# Data structures
class Sprint:
    def __init__(self):
        self.point_completion_history = []

class TeamMember:
    def __init__(self, name, days_off, ceremonies_commitment, hours_per_day_range):
        self.name = name
        self.days_off = days_off
        self.ceremonies_commitment = ceremonies_commitment
        self.hours_per_day_range = hours_per_day_range

class Team:
    def __init__(self):
        self.members = []
