import logging
from turtle import Turtle, Screen

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

        
def flying_turtle(scf):
    """
    Create a turtle on screen that links to our drone and draws the drones flight path.
    """
    # Create instance of crazyflie and take off 
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        screen = Screen()
        donatello = Turtle(shape="turtle")
        donatello.shapesize(2)
        donatello.pensize(5)
        donatello.speed(1)

        screen.exitonclick()

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:        
        # Run flight function
        print("Getting ready to fly")
        flying_turtle(scf)
        print("Landed safe and sound!")
 