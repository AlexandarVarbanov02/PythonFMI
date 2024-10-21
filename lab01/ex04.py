from typing import Tuple, Dict, List


class Turtle:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__move_counter = 0 # Keeping track of the amount of moves == len(__drawing)
        self.__x = x
        self.__y = y
        self.__drawing = list() # History of moves done
        self.__configuration = dict() # Configuration set in configure_turtle method

    def __str__(self) -> str:
        return f"Turtle is at position ({self.__x},{self.__y}) and has moved {self.__move_counter} times since start"

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def moves(self) -> List[str]:
        return self.__drawing

    def get_current_position(self) -> Tuple[int, int]:
        return self.__x, self.__y

    def move(self, *args: int) -> None:
        possible_moves = {"up": (0,1), "down": (0,-1), "left": (-1,0), "right": (1,0)}
        for command in args:
            # Is (0,0) one of my corners or the center of the screen?
            # Assuming is the center. Otherwise, I need to check if position is out of bounds and do different calcs.
            if command not in possible_moves.keys():
                print(f"Invalid command: {command}")
                continue

            for key, value in possible_moves.items():
                if key == command:
                    self.__x += value[0]
                    self.__y += value[1]
                    self.__move_counter += 1
                    self.__drawing.append(key)

    def configure_turtle(self, **kwargs: Dict[str, str]) -> str:
        self.__configuration = kwargs
        config_pairs = [f"{key}:{value}" for key, value in self.__configuration.items()]
        return "Current configuration: " + " | ".join(config_pairs) + " |"
        # Adding "|" at the back because of format. I guess its supposed to be done with a cycle

    def check_for_drawing(self, moves: List[str]) -> bool:
        if len(moves) > len(self.__drawing):
            return False

        for i in range(len(self.__drawing) - len(moves) + 1):
            if self.__drawing[i:i + len(moves)] == moves:
                return True

        return False

# Test Case 1: Test Turtle Initialization with default coordinates (0, 0)
t1 = Turtle()
assert t1.x == 0 and t1.y == 0, "Initial position should be (0,0)"
assert str(t1) == "Turtle is at position (0,0) and has moved 0 times since start", "String representation is incorrect"

# Test Case 2: Test move method with valid moves
t1.move('up', 'right', 'down', 'left')
assert t1.x == 0 and t1.y == 0, "Turtle should return to (0,0) after up, right, down, left"
assert len(t1.moves) == 4, "Turtle should have 4 moves recorded"
assert str(t1) == "Turtle is at position (0,0) and has moved 4 times since start", "String representation after 4 moves is incorrect"

# Test Case 3: Test move method with invalid move
t1.move('right', 'testing', 'right', 'left')
assert len(t1.moves) == 7, "Invalid move should not be added to the move list"
assert str(t1) == "Turtle is at position (1,0) and has moved 7 times since start", "Invalid move should not affect the position or count of moves"

# Test Case 4: Test Turtle Initialization with custom coordinates
t2 = Turtle(3, 4)
assert t2.x == 3 and t2.y == 4, "Initial position should be (3,4)"
assert str(t2) == "Turtle is at position (3,4) and has moved 0 times since start", "String representation with custom initial coordinates is incorrect"

# Test Case 5: Test move method with different valid moves
t2.move('up', 'up', 'right')
assert t2.x == 4 and t2.y == 6, "Turtle should be at (4,6) after moving up twice and right"
assert len(t2.moves) == 3, "Turtle should have 3 moves recorded"
assert str(t2) == "Turtle is at position (4,6) and has moved 3 times since start", "String representation after custom moves is incorrect"

# Test Case 6: Test configure_turtle method
config_message = t2.configure_turtle(color="green", thickness=2, size=10)
assert config_message == "Current configuration: color:green | thickness:2 | size:10 |", "Configuration message is incorrect"

# Test Case 7: Test check_for_drawing method with existing drawing
t2.move('down', 'down', 'left')
assert t2.check_for_drawing(['up', 'right', 'down']) is True, "Drawing sequence should match recorded moves"
assert t2.check_for_drawing(['up', 'up', 'right', 'left']) is False, "Invalid drawing sequence should not match recorded moves"

# Test Case 8: Test get_current_position method
assert t2.get_current_position() == (3, 4), "Current position should be (3,4) after initial moves"