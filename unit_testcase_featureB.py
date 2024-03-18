import unittest
from code1 import Sprint, TeamMember, Team, calculate_available_effort_hours_per_person, calculate_available_effort_hours_for_team

class TestFeatureB(unittest.TestCase):
    def setUp(self):
        # Set up team members and team
        self.team_member1 = TeamMember(name="darshini", days_off=1, ceremonies_commitment=1, hours_per_day_range=[6, 8])
        self.team_member2 = TeamMember(name="pavan", days_off=2, ceremonies_commitment=2, hours_per_day_range=[7, 9])
        self.team = Team()
        self.team.members = [self.team_member1, self.team_member2]

    def test_available_effort_hours_per_person(self):
        # Test individual capacity calculation for each team member
        expected_capacity = 21  # Based on calculations in main code
        expected_capacity_2 = 8
        self.assertEqual(calculate_available_effort_hours_per_person(self.team_member1), expected_capacity)
        self.assertEqual(calculate_available_effort_hours_per_person(self.team_member2), expected_capacity_2)
        
    def test_available_effort_hours_for_team(self):
        # Test available effort-hours for the team
        expected_team_capacity = 29  # Based on calculations in main code
        self.assertEqual(calculate_available_effort_hours_for_team(self.team), expected_team_capacity)

if __name__ == '__main__':
    unittest.main()
