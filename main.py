from pypot.creatures import PoppyErgoJr
import pypot
from Robot import Robot
# Close all connections.
pypot.vrep.close_all_connections()
# Init Poppy in robot object.
robot = Robot(PoppyErgoJr())
# Make it dance !
robot.dance('')

