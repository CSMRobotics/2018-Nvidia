import evdev
import time

def read_devices():
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    for device in devices:
        print(device.fn, device.name)

def get_all_buttons():
    for event in angle.read_loop():
        if event.type == evdev.ecodes.EV_KEY:
            print(evdev.categorize(event))

def read_button(button_event):
    if button_event != None:
        return button_event.code

def read_angle(angle_event):
    if angle_event != None:
        if angle_event.code == 4:
            return angle_event.value * 0.9

def get_wheel_angle_loop():
    for event in angle.read_loop():
        if event.code == 4:
            print('Angle: {}'.format(event.value * 0.9))

def drive(buttons, angle):
    button_event = buttons.read_one()
    angle_event = angle.read_one()

    button_code = read_button(button_event)
    state = "Idle"
    if button_code == 258:
        state = "GO"
    if button_code == 305:
        print('Quit')
        return

    wheel_angle = read_angle(angle_event)
    print("State: {} \t Angle: {}".format(state, wheel_angle))

buttons = evdev.InputDevice('/dev/input/event17')
angle = evdev.InputDevice('/dev/input/event15')
print(buttons.name)
print(buttons.capabilities())
print(angle.name)
print(angle.capabilities())

while(True):
    # event = buttons.read_one()
    # if event != None:
    #     print(event.code)
    # time.sleep(0.1)
    drive(buttons, angle)
