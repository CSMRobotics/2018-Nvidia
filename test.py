from MotorControl import MotorControl


mc = MotorControl()

right_address = 128
left_address = 129
front_address = 130

controller_addresses = mc.list_controllers()
if not (controller_addresses.__contains__(right_address) and controller_addresses.__contains__(left_address) and controller_addresses.__contains__(front_address)):
    exit()


# code goes here