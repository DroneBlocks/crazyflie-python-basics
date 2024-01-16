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

        
def take_off_simple(scf):
    """
    Simple take off, hover for 3 seconds, land, function with MotionCommander
    """
    # Create instance of crazyflie and take off 
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        # Hover for 3 seconds
        time.sleep(3)
        # Stop flight
        mc.stop()


if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:        
        # Run flight function
        print("Getting ready to fly")
        take_off_simple(scf)
        print("Landed safe and sound!")
 