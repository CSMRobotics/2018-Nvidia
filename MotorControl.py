from roboclaw import Roboclaw
import platform


class MotorControl:
    def __init__(self, rate=115200, timeout=0.01, retries=3):
        self.rate = rate
        self.timeout = timeout
        self._trystimeout = retries
        self._crc = 0
        self.baseStr = "/dev/ttyACM"
        if platform.system() == "Windows":
            self.baseStr = "COM"
        self.controller_dictionary, self.speed_factors = self.find_controllers()

    def find_controllers(self):

        addressList = [0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87]

        controller_dictionary = {}
        speed_factors = {}
        for i in range(0, 9):
            rc = Roboclaw(self.baseStr + str(i), self.rate)
            if rc.Open() == 0:
                for a in addressList:
                    if rc.GetConfig(a) != (0, 0):
                        controller_dictionary[a] = rc
                        speed_factors[a] = [1, 1, 1]
                        break
        return controller_dictionary, speed_factors

    def list_controllers(self):
        return self.controller_dictionary.keys()

    def set_control_speed_factors(self, address, factor):
        self.speed_factors[address][0] = factor

    def set_motor_speed_factors(self, address, m1_factor, m2_factor):
        self.speed_factors[address][1] = m1_factor
        self.speed_factors[address][2] = m2_factor

    def drive_M1(self, address, speed):
        rc = self.controller_dictionary.get(address)
        rc.ForwardBackwardM1(address, int((speed * 63 * self.speed_factors[address][0] * self.speed_factors[address][1])) + 64)

    def drive_M2(self, address, speed):
        rc = self.controller_dictionary.get(address)
        rc.ForwardBackwardM2(address, int((speed * 63 * self.speed_factors[address][0] * self.speed_factors[address][2])) + 64)

    def drive_both(self, address, speed):
        rc = self.controller_dictionary.get(address)
        rc.ForwardBackwardM1(address, int((speed * 63 * self.speed_factors[address][0] * self.speed_factors[address][1])) + 64)
        rc.ForwardBackwardM2(address, int((speed * 63 * self.speed_factors[address][0] * self.speed_factors[address][2])) + 64)
