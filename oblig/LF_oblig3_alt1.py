__author__ = 'Fahrvergnugen'


def hours(seconds: int = 0, is_24: bool = True) -> int:
    """Translates integer seconds to hours after midnight.

    args:
        seconds (int) : seconds from midnight
        is_24 (bool) : True for 24-hour format, False for 12-hour
    return:
        hours after midnight from seconds
    """
    """
    hours = seconds // 3600
    if is_24:
        return hours % 24
    else:
        return hours % 12 or 12
    """
    return (seconds // 3600) % 24 if is_24 else (seconds // 3600) % 12 or 12


def minutes(seconds: int = 0) -> int:
    """Minutes in the _last_ hour in time since midnight.

    args:
        seconds (int) : seconds since midnight
    returns:
        (int) minutes in last hour since midnight
    """
    time = seconds - 3600*hours(seconds)
    return time // 60

    minutter = (seconds // 60) % 60
    return minutter

def lamp(digit: int) -> list:
    """Returns a list of bools to light a 7-digit matrix led.

    args:
        digit (int) : Digit to translate to matrix
    return:
        (list) list of booleans marking lit segments.
    """
    arr = [0]*7

    arr[0] = 1 if digit in [0, 2, 3, 5, 6, 7, 8, 9] else 0
    arr[1] = 1 if digit in [0, 1, 2, 3, 4, 7, 8, 9] else 0
    arr[2] = 1 if digit in [2, 3, 4, 5, 6, 8, 9] else 0
    arr[3] = 1 if digit in [0, 4, 5, 6, 8, 9] else 0
    arr[4] = 1 if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else 0
    arr[5] = 1 if digit in [0, 2, 3, 5, 6, 8, 9] else 0
    arr[6] = 1 if digit in [0, 2, 6, 8] else 0

    return arr


def showClock(seconds_from_midnight: int = 0, is_24: bool = True) -> list:
    """Takes seconds from midnight and translates to a matrix to control
    lights for a 7-segment-type display.

    args:
        seconds_from_midnight (int) : seconds from midnight.
        is_24 (bool) : True for a 24-hour format clock, False for 12-hour
    """

    timer = hours(seconds_from_midnight, is_24)
    minutter = minutes(seconds_from_midnight)
    segments = [None, None, None, None]

    if timer < 10:
        segments[0] = lamp(0)
        segments[1] = lamp(timer)
    else:
        timer = str(timer)
        segments[0] = lamp(int(timer[0]))
        segments[1] = lamp(int(timer[1]))

    if minutter < 10:
        segments[2] = lamp(0)
        segments[3] = lamp(minutter)
    else:
        minutter = str(minutter)
        segments[2] = lamp(int(minutter[0]))
        segments[3] = lamp(int(minutter[1]))

    return segments



print(
    showClock(50220, True) == \
        [[0, 1, 0, 0, 1, 0, 0], [1, 1, 1, 0, 1, 1, 0],
        [1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 0, 1, 0, 0]]
)