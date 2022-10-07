import subprocess


class IBeacon:

    def execute_command(self, command):
        subprocess.run(command, shell=True)
        print(command)

    def hexify(self, i, digits=2):
        format_string = "0%dx" % digits
        return format(i, format_string).upper()

    def hexsplit(self, string):
        return ' '.join([string[i:i + 2] for i in range(0, len(string), 2)])

    def execute_beacon(self, uuid: str, major: int, minor: int, power: str):
        # uuid = "AA BB CC DD EE FF 99 / 00 00 00 00 00 00 00 / 00 01"
        '''uuid = "aabbccddeeff99000000000000000001"
        major = 0
        minor = 0'''
        power = int(power, 16)
        device = "hci0"

        uuid = self.hexsplit(uuid.upper())

        major = self.hexify(major, 4)
        minor = self.hexify(minor, 4)

        major = self.hexsplit(major)
        minor = self.hexsplit(minor)

        power = self.hexify(power, 2)

        # uuid = "AA BB CC DD EE FF 99 00 00 00 00 00 00 00 00 01 00 00 00 00 BA"
        print(uuid, major, minor, power)

        '''self.execute_command("sudo hciconfig %s up" % device)

        self.execute_command("sudo hciconfig %s leadv" % device)

        # self.execute_command("sudo hciconfig %s noscan" % device)

        self.execute_command(
            "sudo hcitool -i %s cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 %s %s %s %s 00 >/dev/null" % (
                device, uuid, major, minor, power))'''
