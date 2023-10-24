import unittest
import logging
import datetime

from typing import List
from TheMartianRobot import Planet
from TheMartianRobot import Robot

# Configure logging settings
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='tests\\logs\\unit_testing.log',
    filemode="w")

# Unit testing the move function in the Robot class
class TestRobotMoveFunction(unittest.TestCase):
    
    def setUp(self):
        # Set up a Planet instance for the tests
        self.planet = Planet(5, 3)
    
    def test_move_within_bounds(self):
        logging.info(f"Starting test: test_move_within_bounds {datetime.datetime.now()}")
        robot = Robot(2, 2, "N", self.planet)
        robot.move()
        self.assertEqual((robot.x, robot.y), (2, 3))
        logging.info(f"Completed test: test_move_within_bounds {datetime.datetime.now()}")
    
    def test_move_out_of_bounds_without_scent(self):
        logging.info(f"Starting test: test_move_out_of_bounds_without_scent {datetime.datetime.now()}")
        robot = Robot(5, 3, "N", self.planet)
        robot.move()
        self.assertEqual((robot.x, robot.y), (5, 3))
        self.assertTrue(robot.lost)
        logging.info(f"Completed test: test_move_out_of_bounds_without_scent {datetime.datetime.now()}")
    
    def test_move_out_of_bounds_with_scent(self):
        logging.info(f"Starting test: test_move_out_of_bounds_with_scent {datetime.datetime.now()}")
        # First robot leaves a scent
        robot1 = Robot(5, 3, "N", self.planet)
        robot1.move()
        self.assertTrue(robot1.lost)
        
        # Second robot tries to move to the same position        
        robot2 = Robot(5, 3, "N", self.planet)
        robot2.move()
        self.assertEqual((robot2.x, robot2.y), (5, 4))
        self.assertFalse(robot2.lost)
        logging.info(f"Completed test: test_move_out_of_bounds_with_scent {datetime.datetime.now()}")
    
    def test_move_in_all_directions(self):
        logging.info(f"Starting test: test_move_in_all_directions {datetime.datetime.now()}")
        directions = ["N", "E", "S", "W"]
        expected_positions = [(2, 3), (3, 2), (2, 1), (1, 2)]
        
        for direction, expected_position in zip(directions, expected_positions):
            robot = Robot(2, 2, direction, self.planet)
            robot.move()
            self.assertEqual((robot.x, robot.y), expected_position)

        logging.info(f"Completed test: test_move_in_all_directions {datetime.datetime.now()}")

# Run the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestRobotMoveFunction))
print("Finished testing Robots.Move...")

# Unit testing the execute_instruction function in the Robot class
class TestRobotExecuteInstruction(unittest.TestCase):
    
    def setUp(self):
        # Set up a Mars instance for the tests
        self.planet = Planet(5, 3)
    
    def test_execute_turn_left(self):
        logging.info(f"Starting test: test_execute_turn_left {datetime.datetime.now()}")
        robot = Robot(2, 2, "N", self.planet)
        robot.execute_instruction("L")
        self.assertEqual(robot.direction, "W")
        logging.info(f"Completed test: test_execute_turn_left {datetime.datetime.now()}")
    
    def test_execute_turn_right(self):
        logging.info(f"Starting test: test_execute_turn_right {datetime.datetime.now()}")
        robot = Robot(2, 2, "N", self.planet)
        robot.execute_instruction("R")
        self.assertEqual(robot.direction, "E")
        logging.info(f"Completed test: test_execute_turn_right {datetime.datetime.now()}")
    
    def test_execute_move_forward(self):
        logging.info(f"Starting test: test_execute_move_forward {datetime.datetime.now()}")
        robot = Robot(2, 2, "N", self.planet)
        robot.execute_instruction("F")
        self.assertEqual((robot.x, robot.y), (2, 3))
        logging.info(f"Completed test: test_execute_move_forward {datetime.datetime.now()}")

# Run the tests with logging
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestRobotExecuteInstruction))
print("Finished testing Robots.execute_instructions...")

# Input Testing
# Define instructions processor
def process_instructions(instructions: List[str]) -> List[str]:
    # Extracting the grid dimensions
    width, length = map(int, instructions[0].split())
    mars = Planet(width, length)

    # Process robot instructions
    outputs = []
    for i in range(1, len(instructions), 2):
        x, y, direction = instructions[i].split()
        robot = Robot(int(x), int(y), direction, mars)
        for instruction in instructions[i + 1]:
            robot.execute_instruction(instruction)
        if robot.lost:
            outputs.append(f"{robot.x} {robot.y} {robot.direction} LOST")
        else:
            outputs.append(f"{robot.x} {robot.y} {robot.direction}")

    return outputs

# Define the test cases and expected outputs
test_cases = [
    {
        "input": ["5 3", "1 1 E", "RFRFRFRF", "3 2 N", "FRRFLLFFRRFLL", "0 3 W", "LLFFFLFLFL"],
        "expected_output": ["1 1 E", "3 3 N LOST", "2 3 S"]
    },
    {
        "input": ["5 3", "2 2 N", "LRLRLRLR"],
        "expected_output": ["2 2 N"]
    },
    {
        "input": ["5 3", "5 3 N", "FFFFFFFFF"],
        "expected_output": ["5 3 N LOST"]
    },
    {
        "input": ["5 3", "5 3 N", "F", "5 3 N", "F", "5 3 N", "F"],
        "expected_output": ["5 3 N LOST", "5 3 N", "5 3 N"]
    }
]

# Run the test cases using assert
for idx, test_case in enumerate(test_cases, 1):
    logging.info(f"Starting Test Case {idx} {datetime.datetime.now()}")
    output = process_instructions(test_case["input"])
    if output != test_case["expected_output"]:
        logging.error(f"Test Case {idx} Failed! {datetime.datetime.now()}")
        logging.error(f"Expected: {test_case['expected_output']} {datetime.datetime.now()}")
        logging.error(f"Got: {output}")
    else:
        logging.info(f"Completed Test Case {idx} {datetime.datetime.now()}")

print("Finished testing inputs...")
