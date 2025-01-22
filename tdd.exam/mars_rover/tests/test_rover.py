# tests/test_rover.py

import pytest
from src.rover import Rover
from src.plateau import Plateau

def test_rover_movement():
    plateau = Plateau(5, 5)
    rover = Rover(1, 2, "N", plateau)
    rover.execute_commands("LMLMLMLMM")
    assert rover.get_position() == (1, 3, "N")

    rover = Rover(3, 3, "E", plateau)
    rover.execute_commands("MMRMMRMRRM")
    assert rover.get_position() == (5, 1, "E")
