from MotorControl import MotorControl
import time

mc = MotorControl()

right_address = 128
left_address = 129
front_address = 130


controller_addresses = mc.list_controllers()
print(controller_addresses)

#if not (controller_addresses.__contains__(right_address) and controller_addresses.__contains__(left_address) and controller_addresses.__contains__(front_address)):
    #exit()

time.sleep(5)

mc.drive_both(right_address, 1)
mc.drive_both(left_address, 1)
#mc.drive_M2(front_address, 1)
time.sleep(5)

mc.drive_both(right_address, -1)
mc.drive_both(left_address, -1)
#mc.drive_M2(front_address, -1)
time.sleep(5)

mc.drive_both(right_address, 0)
mc.drive_both(left_address, 0)
#mc.drive_M2(front_address, 0)

# code goes here