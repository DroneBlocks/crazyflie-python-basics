# TODO: #1 WATCH LESSON 04-01 WHAT YOU WILL BUILD
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

# TODO: #2 CREATE FUNCTION THAT ASKS FOR INPUT AND ONLY ACCEPTS INTEGER 

def move_in_user_defined_shape(scf):
    """ Simple function that flies in a shape based on user input for number of sides.
        Number of sides is divided by 360 to work out rotation angle. 

        :param user_input: Number of sides of shape.
    """

    # TODO: #3 TAKE USER_INPUT AND CALCULATE TURN_LEFT ANGLE FOR INTERIOR ANGLE OF SHAPE

    
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(1)
        # TODO: #4 FLY FORWARD, SLEEP, TURN_LEFT(X) FOR EACH SIDE OF SHAPE      
        time.sleep(0.5)


if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        move_in_user_defined_shape(scf)


# TODO: #5 ADD COMMENTS TO CODE