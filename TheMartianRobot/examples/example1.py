from typing import List
from TheMartianRobot import Planet
from TheMartianRobot import Robot

# define a new planet "Mars" with a grid size of 50x50
mars = Planet(name="Mars", width=50, length=50)

# send a new robot on the mission
gtron = Robot(x=1, y=1, direction="N", planet=mars)

# move the robot
gtron.move()
print(gtron)  # Should display: "2 1 N"

# turn the robot left
gtron.turn_left()
print(gtron)  # Should display: "2 1 W"

# turn the robot right
gtron.turn_right()
print(gtron)  # Should return back to: "2 1 N"

# executing a sequence of instructions
instructions = "LFR"
for instruction in instructions:
    gtron.execute_instruction(instruction)

# display the robot's final position and direction after executing the instructions
print(gtron)

# checking if robot is lost?
if gtron.lost:
    print("gtron is lost!")
else:
    print("gtron is still operational.")
