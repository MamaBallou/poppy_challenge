from pypot.creatures import PoppyErgoJr
import pypot
from Robot import Robot
# Close all connections.
pypot.vrep.close_all_connections()
# Init Poppy in robot object.
robot = Robot(PoppyErgoJr(simulator='vrep', scene='poppy_ergo_jr_holder.ttt'))
# Make it dance !
robot.dance('')