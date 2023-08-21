from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])


NORTH, EAST, SOUTH, WEST = 1, 2, 4, 8
DELTA = {
    1: Point(0, 1),
    2: Point(1, 0),
    4: Point(0, -1),
    8: Point(-1, 0),
}


class Robot(object):
    """A robot capable of moving around a grid.

    Attributes:
        * bearing (int): numerical representation of the robot's
            orientation based on cardinal direction configuration.
    """

    def __init__(
        self, direction: int = NORTH, starting_x: int = 0, starting_y: int = 0
    ) -> None:
        self.direction = direction
        self._coordinates = Point(starting_x, starting_y)

    @property
    def coordinates(self) -> Point:
        """Return the robot's coordinates as Point(x, y)."""
        return self._coordinates

    def turn_left(self) -> None:
        """Uses bit manipulation to orient the robot."""
        self.direction = (self.direction << 3) % 15

    def turn_right(self) -> None:
        """Uses bit manipulation to orient the robot."""
        self.direction = (self.direction << 1) % 15

    def advance(self) -> None:
        """Alter coordinates based on the robot's direction."""
        self._coordinates = self._coordinates._replace(
            x=(self._coordinates.x + DELTA[self.direction].x),
            y=(self._coordinates.y + DELTA[self.direction].y),
        )

    def move(self, path: str) -> None:
        """Moves the robot along the given path.

        Path can be defined with combinations of three commands:
            * 'L': turn left
            * 'R': turn right
            * 'A': move forward one grid unit

        :params path: str - instructions for the robot's movement.
        """
        execute = {
            "L": self.turn_left,
            "R": self.turn_right,
            "A": self.advance,
        }
        for step in path:
            execute[step]()
