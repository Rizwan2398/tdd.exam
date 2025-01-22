# src/main.py

from src.plateau import Plateau
from src.rover import Rover

def main():
    # Entrée utilisateur
    plateau_input = input("Enter plateau dimensions: ")
    plateau_size = list(map(int, plateau_input.split()))
    plateau = Plateau(plateau_size[0], plateau_size[1])

    while True:
        try:
            rover_position = input("Enter rover position (or press Enter to quit): ")
            if not rover_position:
                break
            x, y, direction = rover_position.split()
            rover = Rover(int(x), int(y), direction, plateau)

            commands = input("Enter movement commands: ")
            rover.execute_commands(commands)

            print(f"Rover final position: {rover.get_position()}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
