#import cv2
#import matplotlib.pyplot as plt
from pypot.creatures import PoppyErgoJr
import pypot
from Robot import Robot
# Init Poppy
pypot.vrep.close_all_connections()
robot = Robot(PoppyErgoJr(simulator='vrep', scene="poppy_ergo_jr_holder.ttt"))
robot.dance()




"""
poppy.m1.goto_position(0, 2)
poppy.m2.goto_position(0, 2)
poppy.m3.goto_position(0, 2)
poppy.m4.goto_position(0, 2)
poppy.m5.goto_position(0, 2)
poppy.m6.goto_position(0, 2, wait = True)

poppy.m1.goto_position(-150, 5)
poppy.m5.goto_position(0, 5, wait = True)

poppy.m1.goto_position(-100, 5)
poppy.m5.goto_position(90, 5, wait = True)

poppy.m1.goto_position(-50, 5)
poppy.m5.goto_position(0, 5, wait = True)

poppy.m1.goto_position(0, 5)
poppy.m5.goto_position(90, 5, wait = True)

poppy.m1.goto_position(100, 5)
poppy.m5.goto_position(0, 5, wait = True)

poppy.m1.goto_position(150, 5)
poppy.m5.goto_position(90, 5, wait = True)

poppy.m1.goto_position(0, 20)
poppy.m2.goto_position(-90, 20)
poppy.m3.goto_position(0, 20)
poppy.m4.goto_position(0, 20)
poppy.m5.goto_position(90, 20)
poppy.m6.goto_position(0, 20, wait = True)

poppy.m1.goto_position(0, 20)
poppy.m2.goto_position(0, 20)
poppy.m3.goto_position(-90, 20)
poppy.m4.goto_position(0, 20)
poppy.m5.goto_position(-90, 20)
poppy.m6.goto_position(0, 20, wait = True)
# Init IKPy
poppy.chain.end_effector
zero = [0]*6
ax = plt.figure().add_subplot(111, projection='3d')
poppy.chain.plot(poppy.chain.convert_to_ik_angles(zero), ax)

listToVisit = AlgoVoisin.algoVoisin()
for pos in listToVisit:
    print(len(pos))
    pos = 0.1*np.asarray([float(pos[0]), float(pos[1]), float(pos[2])])
    print(pos)
    poppy.chain.goto(pos, 2., True, True)
#img=poppy.camera.frame
#plt.imshow(cv2.cvtColor(img.cv2.COLOR_BGR2RGB))
"""