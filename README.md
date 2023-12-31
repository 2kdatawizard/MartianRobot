# MartianRobot
This is year 2149, earth seemed like a distant memory and the human race had not only merged with machines but had also found a new home on the red planet.
Mars had its challenges. The unpredictable sandstorms, the vast desolate plains, and the cliffs that dropped into the abyss. To navigate this rugged terrain, robots were created, each equipped with state-of-the-art navigation systems and learning algorithms. These robots, many the size of small cars, roamed the Martian landscapes, carrying out tasks, exploring new territories, and setting up bases for further human-machine expansion.

This project simulates the movement of robots on the surface of Mars, which is represented as a rectangular grid. Robots can move around the grid based on instructions provided, and if a robot moves off the edge of the grid, it is considered "lost". The position where a robot is lost leaves a "scent", preventing future robots from getting lost at the same position.

## Classes Overview

### 1. Planet Class
This class represents the surface of Mars as a rectangular grid. It provides methods to:
- Check if a position on the grid has a "scent" indicating a previously lost robot.
- Mark a position with a "scent" when a robot is lost.

name (str): The name of the planet. Default value is "Mars".<br>
width (int): The width of the planet's grid. Default value is 50.<br>
length (int): The length of the planet's grid. Default value is 50.<br>
robot_scent (set): A set storing the coordinates where robots have left a "scent" due to being lost.

### Methods
```python
# Adds a scent flag at the specified grid coordinates.
add_scent_flag(x: int, y: int) -> None:
Parameters
x (int): The x-coordinate of the grid position.
y (int): The y-coordinate of the grid position.

# Checks if a specific grid position has a scent.
is_scented(x: int, y: int) -> bool:
Parameters
x (int): The x-coordinate of the grid position.
y (int): The y-coordinate of the grid position.
```

Initialize a planet with default parameters:
```python
mars = Planet()
```
Add a scent flag at a specific position (e.g., x=10, y=20):
```python
mars.add_scent_flag(10, 20)
```
Check if a specific position has a scent (e.g., x=10, y=20):
```python
if mars.is_scented(10, 20):
    print("The position has a scent!")
else:
    print("The position doesn't have a scent.")
```

### 2. Robot Class
The Robot class simulates a robot's movement on a planet's surface. Each robot has a position defined by its x and y coordinates and a direction it's facing. The robot can turn left, turn right, or move forward in the direction it's currently facing. If a robot moves to a position where a previous robot was lost, it leaves a "scent" on that position, and any subsequent robots will recognize this scent and avoid getting lost at the same location.

### Attributes
**x** (int): The x-coordinate of the robot's position.<br>
**y** (int): The y-coordinate of the robot's position.<br>
**direction** (str): The current direction the robot is facing. It can be "N" (North), "E" (East), "S" (South), or "W" (West).<br>
**planet** (Planet): The planet object on which the robot is operating.<br>
**lost** (bool): A flag indicating whether the robot is lost.

### Constants
**DIRECTION** (List[str]): List of all possible directions a robot can face.<br>
**LEFT_TURNS** (Dict[str, str]): Dictionary mapping the current direction to the direction after a left turn.<br>
**RIGHT_TURNS** (Dict[str, str]): Dictionary mapping the current direction to the direction after a right turn.

### Methods
```python
move() -> None: # Moves the robot forward in its current direction.
turn_left() -> None: # Turns the robot 90 degrees to the left without changing its position.
turn_right() -> None: # Turns the robot 90 degrees to the right without changing its position.
execute_instruction(instruction: str) -> None: # Executes a given instruction (either move forward, turn left, or turn right).
```
## How to Run the Code
To simulate the movement of robots based on a set of instructions, use the ```process_instructions``` function in the ```tests\UnitTesting.py```. Provide it with a list of strings representing the instructions, and it will return the final positions of the robots.

```python
instructions = ["5 3", "1 1 E", "RFRFRFRF", "3 2 N", "FRRFLLFFRRFLL", "0 3 W", "LLFFFLFLFL"]
output = process_instructions(instructions)
print(output)
```
## How to Run Tests
The codebase includes unit tests for the Robot's movement methods and the `process_instructions` function. Use the respective test classes to run these tests. These are available under the ```test``` folder

## Notes
- The project uses logging to capture detailed information about the test execution. The log file `unit_testing.log` contains these logs.
- Always ensure that the Planet and Robot classes are defined before running the main logic or tests.
