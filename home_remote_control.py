from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class NoCommand(Command):
    def execute(self):
        pass


class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class Remote:
    on_command = [NoCommand] * 3
    off_command = [NoCommand] * 3

    def set_on_command(self, slot, command: Command):
        self.on_command[slot] = command

    def set_off_command(self, slot, command: Command):
        self.off_command[slot] = command

    def press_on_button(self, slot):
        self.on_command[slot].execute()

    def press_off_button(self, slot):
        self.off_command[slot].execute()


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()


def main():
    r = Remote()
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    r.set_on_command(0, light_on)
    r.set_off_command(1, light_off)
    r.press_on_button(0)
    r.press_off_button(1)


if __name__ == '__main__':
    main()
