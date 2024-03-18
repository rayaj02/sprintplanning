import unittest
from code1 import Sprint, calculate_average_velocity

class TestFeatureA(unittest.TestCase):
    def test_empty_point_completion_history(self):
        sprint = Sprint()
        sprint.point_completion_history = []
        self.assertEqual(calculate_average_velocity(sprint), 0)

    def test_non_empty_point_completion_history(self):
        sprint = Sprint()
        sprint.point_completion_history = [10, 15, 20]
        self.assertEqual(calculate_average_velocity(sprint), 15)  # Average of [10, 15, 20] is 15

    def test_zero_velocity(self):
        sprint = Sprint()
        sprint.point_completion_history = [0, 0, 0]
        self.assertEqual(calculate_average_velocity(sprint), 0)

    def test_negative_point_completion_history(self):
        sprint = Sprint()
        sprint.point_completion_history = [-10, -15, -20]
        self.assertEqual(calculate_average_velocity(sprint), -15)  # Average of [-10, -15, -20] is -15

if __name__ == '__main__':
    unittest.main()

