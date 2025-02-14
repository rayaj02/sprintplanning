# acceptance_test_for_featureA.py

# Import the Sprint class and the function to be tested
from code1 import Sprint, test calculate_average_velocity

# Define the acceptance test
def test_calculate_average_velocity():
    # Scenario: Calculate average velocity for a sprint with points completion history
    sprint = Sprint()
    sprint.point_completion_history = [10, 15, 20]

    # Expected result based on the data provided
    expected_average_velocity = (10 + 15 + 20) / 3  # Sum of points completed divided by number of sprints

    # Calculate the actual result
    actual_average_velocity = calculate_average_velocity(sprint)

    # Verify if the actual result matches the expected result
    assert actual_average_velocity == expected_average_velocity, f"Expected: {expected_average_velocity}, Got: {actual_average_velocity}"

    print("Feature A acceptance test passed successfully.")

# Execute the acceptance test
if __name__ == "__main__":
    test_calculate_average_velocity()
