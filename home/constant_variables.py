class Speed:
    """Speed"""
    LOW_SPEED = 0
    MEDIUM_SPEED = 1
    HIGH_SPEED = 2

class OnAndOff:
    """ON AND OFF"""
    ON = 1
    OFF = -1

class Sensor:
    """SENSOR"""
    IN_1 = 24
    IN_2 = 23
    EN = 25
    TEMP1 = 1

class Membrane_Switch:
    """MEMBRANE SWITCH BUTTON"""
    # color index
    RED = 0
    YELLOW = 1
    GREEN = 2

    # gpio pin
    RED_STOP = 14
    YELLOW_CW = 15
    GREEN_CCW = 18

    # for json pin_dict
    PSEUDO_MEMBRANE_SWITCH = {
        'RED_STOP' : RED_STOP,
        'YELLOW_CW': YELLOW_CW,
        'GREEN_CCW' : GREEN_CCW
        }