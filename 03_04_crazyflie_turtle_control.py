# Import required libraries and modules
import logging
from turtle import Turtle, Screen
import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

# Set Uniform Resource Identifier and default height and distance constant
URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
DEFAULT_HEIGHT = 0.3

TURTLE_DISTANCE = 50    
CRAZYFLIE_DISTANCE = 0.1
TURN_ANGLE = 10

logging.basicConfig(level=logging.ERROR)


# Create function to create drone and turtle objects
def turtle_power(scf):
    """
    Creates Drone and Turtle objects and allows user to control crazyflie drone with keyboard keys.
    Use 'w' to move forward, 's' to move backward, 'a' to turn left, and 'd' to turn right.
    Turtle instance moves with drone to visualize flight path.    

    """
    # Opens and closes drone using 'with' statement ensures proper resource management 
    with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
        # Create turtle and screen objects
        screen = Screen()
        donatello = Turtle(shape="turtle")
        donatello.shapesize(2)
        donatello.pensize(5)
        donatello.speed(1)
        
        # Moves turtle and drone forward 
        def move_forward():
            # Move the turtle object and the drone forward by DISTANCE units
            donatello.forward(TURTLE_DISTANCE)
            mc.forward(CRAZYFLIE_DISTANCE)


        def move_backward():
            # Move the turtle object and the drone backward by DISTANCE units
            donatello.backward(TURTLE_DISTANCE)
            mc.back(CRAZYFLIE_DISTANCE)


        def turn_left():
            # Turns the turtle object and the drone left by DISTANCE units
            donatello.left(TURN_ANGLE)
            mc.turn_left(TURN_ANGLE)

        
        def turn_right():
            # Turns the turtle object and the drone right by DISTANCE units
            donatello.right(TURN_ANGLE)
            mc.turn_right(TURN_ANGLE)

        def close_screen():
            # Closes the screen object
            screen.bye()

        # Creates screen object and listens for user input
        screen.listen()
        screen.onkey(key="w", fun=move_forward)
        screen.onkey(key="s", fun=move_backward)
        screen.onkey(key="a", fun=turn_left)
        screen.onkey(key="d", fun=turn_right)
        screen.onkey(key="q", fun=close_screen)
        
        screen.exitonclick()

if __name__ == '__main__':
    # Initialize drivers and create drone object
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        turtle_power(scf)
