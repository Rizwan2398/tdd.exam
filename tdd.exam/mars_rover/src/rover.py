# src/rover.py

class Rover:
    DIRECTIONS = ["N", "E", "S", "W"]

    def __init__(self, x, y, direction, plateau):
        self.x = x
        self.y = y
        self.direction = direction
        self.plateau = plateau

    def turn_left(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) - 1) % 4]

    def turn_right(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + 1) % 4]

    def move_forward(self):
        if self.direction == "N":
            new_y = self.y + 1
            if self.plateau.is_within_bounds(self.x, new_y):
                self.y = new_y
        elif self.direction == "E":
            new_x = self.x + 1
            if self.plateau.is_within_bounds(new_x, self.y):
                self.x = new_x
        elif self.direction == "S":
            new_y = self.y - 1
            if self.plateau.is_within_bounds(self.x, new_y):
                self.y = new_y
        elif self.direction == "W":
            new_x = self.x - 1
            if self.plateau.is_within_bounds(new_x, self.y):
                self.x = new_x

    def execute_commands(self, commands):
        for command in commands:
            if command == "L":
                self.turn_left()
            elif command == "R":
                self.turn_right()
            elif command == "M":
                self.move_forward()

    def get_position(self):
        return self.x, self.y, self.direction
