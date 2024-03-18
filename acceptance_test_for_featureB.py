# acceptance_test_for_featureB.py

# Import the necessary classes and functions from your main code
from code1 import Team, TeamMember, calculate_available_effort_hours_for_team, calculate_available_effort_hours_per_person

# Define the acceptance test for Feature B
def test_feature_b_acceptance():
    # Scenario: Happy path - Calculate available effort-hours for the team and per person
    team_member1 = TeamMember(name="Darshini", days_off=1, ceremonies_commitment=1, hours_per_day_range=[6, 8])
    team_member2 = TeamMember(name="Pavan", days_off=2, ceremonies_commitment=2, hours_per_day_range=[7, 9])
    
    # Create a team with the team members
    team = Team()
    team.members = [team_member1, team_member2]
    
    # Calculate available effort-hours for the team
    team_effort_hours = calculate_available_effort_hours_for_team(team)
    
    # Calculate available effort-hours per person
    darshini_effort_hours = calculate_available_effort_hours_per_person(team_member1)
    pavan_effort_hours = calculate_available_effort_hours_per_person(team_member2)
    
    # Verify the results for the happy path
    assert team_effort_hours == 29, f"Expected team effort-hours: 29, Actual: {team_effort_hours}"
    assert darshini_effort_hours == 21, f"Expected Darshini's effort-hours: 28, Actual: {darshini_effort_hours}"
    assert pavan_effort_hours == 8, f"Expected Pavan's effort-hours: 28, Actual: {pavan_effort_hours}"
    
    print("Happy path for Feature B acceptance test passed.")
    
    # Scenario: Unhappy path - Calculate available effort-hours for an empty team
    empty_team = Team()  # Create an empty team
    
    # Calculate available effort-hours for the empty team
    empty_team_effort_hours = calculate_available_effort_hours_for_team(empty_team)
    
    # Verify the result for the unhappy path
    assert empty_team_effort_hours == 0, f"Expected team effort-hours for empty team: 0, Actual: {empty_team_effort_hours}"
    
    print("Unhappy path for Feature B acceptance test passed.")

# Execute the acceptance test
if __name__ == "__main__":
    test_feature_b_acceptance()
