
"""import matplotlib.pyplot as plt


# Subtask completion status
subtask_completion = {
    'feature_a_subtask1': True,
    'feature_b_subtask1': True,
    'feature_a_subtask2': False,
    'feature_b_subtask2': False,
    'feature_b_subtask3': False,
}

# Sprint Burndown Chart
def plot_burndown_chart(completion_status):
    tasks = list(completion_status.keys())
    remaining_tasks = sum(1 for status in completion_status.values() if not status)

    plt.plot(range(len(tasks)), [remaining_tasks - i for i in range(len(tasks))], marker='o')
    plt.title('Sprint Burndown Chart')
    plt.xlabel('Time (Subtasks Completed)')
    plt.ylabel('Remaining Tasks')
    plt.xticks(range(len(tasks)), tasks, rotation=45)
    plt.show()

# Simulate completion of subtasks
for subtask, status in subtask_completion.items():
    if status:
        continue

    # Simulating completion of subtasks
    print(f"Completing {subtask}")
    subtask_completion[subtask] = True
    plot_burndown_chart(subtask_completion)"""

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

# Feature A - Calculate a sprint team’s velocity
def calculate_average_velocity(sprint):
    if not sprint.point_completion_history:
        return 0
    return sum(sprint.point_completion_history) / len(sprint.point_completion_history)

# Feature B - Calculate Team Effort-Hour Capacity
def calculate_individual_capacity(member):
    total_working_days = 5  # Assuming a standard workweek
    available_days = total_working_days - member.days_off - member.ceremonies_commitment
    hours_per_day = sum(member.hours_per_day_range) / len(member.hours_per_day_range)
    return available_days * hours_per_day

def calculate_total_capacity(team):
    return sum(calculate_individual_capacity(member) for member in team.members)

# New Feature B Subtask - Calculate Available Effort-Hours/Person
def calculate_available_effort_hours_per_person(member):
    return calculate_individual_capacity(member)

# New Feature B Subtask - Calculate Available Effort-Hours for Team
def calculate_available_effort_hours_for_team(team):
    return sum(calculate_available_effort_hours_per_person(member) for member in team.members)

# Input data
sprint = Sprint()
sprint.point_completion_history = [10, 15, 20]

team_member1 = TeamMember(name="darshini", days_off=1, ceremonies_commitment=1, hours_per_day_range=[6, 8])
team_member2 = TeamMember(name="pavan", days_off=2, ceremonies_commitment=2, hours_per_day_range=[7, 9])
team_member3 = TeamMember(name="aswin", days_off=2, ceremonies_commitment=2, hours_per_day_range=[7, 9])
team_member4 = TeamMember(name="jaswanth", days_off=2, ceremonies_commitment=2, hours_per_day_range=[7, 9])

team = Team()
team.members = [team_member1, team_member2]

# Calculate and print results
average_velocity = calculate_average_velocity(sprint)
print(f"Average Velocity: {average_velocity}")

total_capacity = calculate_total_capacity(team)
print(f"Total Team Effort-Hour Capacity: {total_capacity} hours")

# New calculations
available_effort_hours_per_person = calculate_available_effort_hours_per_person(team_member1)
print(f"Available Effort-Hours/Person ({team_member1.name}): {available_effort_hours_per_person} hours")
print(f"Available Effort-Hours/Person ({team_member2.name}): {available_effort_hours_per_person} hours")

print(f"Available Effort-Hours/Person ({team_member3.name}): {available_effort_hours_per_person} hours")

print(f"Available Effort-Hours/Person ({team_member4.name}): {available_effort_hours_per_person} hours")

available_effort_hours_for_team = calculate_available_effort_hours_for_team(team)
print(f"Available Effort-Hours for Team: {available_effort_hours_for_team} hours")
