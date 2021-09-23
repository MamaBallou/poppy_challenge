from pypot.creatures import PoppyErgoJr
import pypot
import time
from Robot import Robot
# Close all connections.
pypot.vrep.close_all_connections()
# Init Poppy in robot object.
robot = Robot(PoppyErgoJr(simulator='vrep', scene="poppy_ergo_jr_holder.ttt"))
# Time start
currentTime = time.time()
# Make it dance !
robot.dance()
# Print lasting
print(time.time() - currentTime)
