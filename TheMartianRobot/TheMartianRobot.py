
class Planet:
    def __init__(self,name:str="mars",width:int=50,length:int=50):
        """
        Initialize a Planet object.
        
        :param name: Name of the planet. Default is "Mars".
        :param width: Width of the planet's grid. Default is 50.
        :param length: Length of the planet's grid. Default is 50.
        """
        self.name = name
        self.width = width
        self.length = length
        self.robot_scent = set() # Store robots scent in a set

    def add_scent_flag(self, x:int, y:int)->None:
        """
        Add a scent flag at the specified coordinates. 
        This indicates a robot has been lost at this position.
        
        :param x: x-coordinate
        :param y: y-coordinate
        """        
        self.robot_scent.add((x, y))

    def is_scented(self, x:int, y:int)->bool:
        """
        Check if a position on the planet has a scent.
        
        :param x: x-coordinate
        :param y: y-coordinate
        :return: True if position is scented, False otherwise.
        """
        return (x, y) in self.robot_scent  

class Robot:
    DIRECTION = ["N","E","S","W"]
    LEFT_TURNS = {
        "N": "W",
        "W": "S",
        "S": "E",
        "E": "N"
    }
    RIGHT_TURNS = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"
    }

    def __init__(self, x:int, y:int, direction:str, planet:Planet):
        self.x = x
        self.y = y
        self.direction = direction
        self.planet = planet
        self.lost = False

    def move(self) -> None:
        # Initialize new positions to the current positions
        new_x, new_y = self.x, self.y
        
        if self.direction == "N":
            new_y += 1
        elif self.direction == "E":
            new_x += 1
        elif self.direction == "S":
            new_y -= 1
        else:
            new_x -= 1

        # check planet grid bounds (edges) and the current position doesn't have a scent
        if not (0 <= new_x <= self.planet.width and 0 <= new_y <= self.planet.length) and not self.planet.is_scented(self.x, self.y):
            self.planet.add_scent_flag(self.x, self.y)
            self.lost = True

        # If the robot is not lost, update its position
        else:
            self.x, self.y = new_x, new_y

    def turn_left(self):
        """
        Turn the robot 90 degrees to the left.
        """
        self.direction = self.LEFT_TURNS[self.direction]

    def turn_right(self):
        """
        Turn the robot 90 degrees to the right.
        """
        self.direction = self.RIGHT_TURNS[self.direction]

    def execute_instruction(self, instruction):
        if self.lost:
            return

        if instruction == "L":
            self.turn_left()
        elif instruction == "R":
            self.turn_right()
        elif instruction == "F":
            self.move()

    def __str__(self):
        # return string output as defined in the problem
        str_x = str(self.x)
        str_y = str(self.y)
        lost_or_not = " LOST" if self.lost else ""
        return str_x + " " + str_y + " " + self.direction + " " + lost_or_not
