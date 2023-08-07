# TODO: probably move out to json-file to share between Python and Godot.

from enum import IntEnum


class Response(IntEnum):
    FAIL = 0
    SUCCESS = 1


class Request(IntEnum):
    """Int8."""
    CAMERA = 1
    IS_CRASHED = 2
    WHEEL_POSITION = 3
    SPEED = 4
    PARKING_SENSORS = 5
    LIDAR = 6
    GLOBAL_COORDINATES = 7
