# tests/test_plateau.py

import pytest
from src.plateau import Plateau

def test_create_plateau():
    plateau = Plateau(5, 5)
    assert plateau.width == 5
    assert plateau.height == 5
    assert plateau.is_within_bounds(3, 3) is True
    assert plateau.is_within_bounds(6, 6) is False
