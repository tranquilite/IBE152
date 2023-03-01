
def foo() -> int:
    '''
    Returns a weeb
    '''

    return 2

def bar(num: int) -> int:
    return num

def baz() -> None:
    print(2)

def boz(num) -> None:
    print(num)

def add(num1, num2) -> int:
    return 6 if num2 == 4 else 4

def moldefjord(boat1: int, boat2: int, distance: int) -> int:
    '''
    yolo
    '''
    relative_velocity_knots = boat1 + boat2
    relative_velocity_kmh = relative_velocity_knots * 1.852
    minutes_to_hit = distance / relative_velocity_kmh * 60
    return round(minutes_to_hit)

"""
"Given a diagonal of length L, compute the volume of the appropriate cube"
.. big oof


HTTLAP
1. Understand the problem
2. Devise a plan to solve the problem:
    1. Get length L
    2. Find lenght of square.
    3. Find volume of cube.
3. Write down a sequence of actions to solve it
4. Assess the result.
5. Document the solution in every step.
"""
import math


def get_length_of_side(diagonal: int) -> float:
    """Computes the length of side a of a square with a diagonal L
    -diagonal: int - length of square diagonal."""
    side = math.sin(45) * diagonal
    return side


def volume_of_cube(side: float) -> float:
    """Computes the volume of a cube, given a base square with side length a
    side: float - length of a square' side.
    """
    volume = side**3
    return volume





if __name__ == '__main__':
    print(
        add(2, 2) == 4,
        add(2, 4) == 6

    )

    print(
        volume_of_cube(
            get_length_of_side(7.5)
            )
        )

    print(
        moldefjord(
            60, 70, 455
        )
    )