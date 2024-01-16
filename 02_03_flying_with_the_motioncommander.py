import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

# Set Uniform Resource Identifier and default height constant
URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
DEFAULT_HEIGHT = 0.3

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


def move_linear_simple(scf):
    """
    Takeoff, fly forward, back, left, right, up and down before landing.
    
    Has a 0.5 second delay between each movement.
    """
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        time.sleep(0.5)
        print("moving forward")
        mc.forward(0.3)
        time.sleep(0.5)
        print("moving back") 
        mc.back(0.3)
        time.sleep(0.5)
        mc.turn_left(90)
        mc.turn_right(180)
        time.sleep(0.5)
        mc.right(0.3)
        time.sleep(0.5)
        mc.up(0.3)
        time.sleep(0.5)
        print("getting tired time to land")
        mc.down(0.3)
        time.sleep(0.5)

if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        # Run flight function
        move_linear_simple(scf)
