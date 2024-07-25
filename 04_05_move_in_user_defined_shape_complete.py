import logging
import time
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

# MAKE SURE YOUR RADIO ADDRESS MATCHES THE CORRECT CRAZYFLIE
DEFAULT_RADIO = 'radio://0/80/2M/E7E7E7E7E7'

# SET UNIFORM RESOURCE IDENTIFIER AND DEFAULT HEIGHT CONSTANT
URI = uri_helper.uri_from_env(default=DEFAULT_RADIO)
DEFAULT_HEIGHT = 0.5

logging.basicConfig(level=logging.ERROR)

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Whoops, that's not a whole number, please enter an integer.")


def move_in_user_defined_shape(scf):
    """ Simple function that flies in a shape based on user input for number of sides.
        Number of sides is divided by 360 to work out rotation angle. 

        :param user_input: Number of sides of shape.
    """
    number_of_sides = get_integer_input("Enter in the number of sides of shape: ")
    side_length = get_integer_input("Enter in the length of sides in CM: ") / 100
    turn_left = 360/number_of_sides

    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(1)
        for _ in range(number_of_sides):
            print("Flying Forward...")
            mc.forward(side_length)
            time.sleep(0.5)
            print("Turning In Progress...")
            mc.turn_left(turn_left)
            time.sleep(0.5)


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        move_in_user_defined_shape(scf)

# TODO: #5 ADD COMMENTS TO CODE