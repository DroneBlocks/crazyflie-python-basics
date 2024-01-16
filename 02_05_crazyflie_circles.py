import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
DEFAULT_HEIGHT = 0.3

logging.basicConfig(level=logging.ERROR)


def move_circle_simple(scf):
    """
    Flies in a circle to the left then right.

    Requires a 1m work area to run successfully.
    
    Has a 0.5 second delay between each movement.
    """
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        # Hover for 1 second
        time.sleep(1)
        # Fly in half circle counter clock wise 
        mc.circle_left(0.2,0.2,180)
        # Hover for 0.5 seconds
        time.sleep(0.5)
        # Fly in half cirlce clock wise
        mc.circle_right(0.2)
        # Hover for 0.5 seconds
        time.sleep(0.5)

if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        print("Taking off!")
        move_circle_simple(scf)
        print("Game Over!!")