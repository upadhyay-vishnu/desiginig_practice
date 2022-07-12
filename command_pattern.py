"""
Command Pattern is an excellent approach of Encapsulation of 
Decouple the requestor of an from the object that actually performs the action.

Here we will implement Remote control, where each segment of button (On, Off) is align to perform
a commad for specific thing, like fan, TV etc.
"""

"""
So there are Command(On, off), reciever(Fan, TV), Actor(Remote), Switch(on, off, undo)
"""

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        NotImplementedError


class Reciever(metaclass=ABCMeta):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class Light(Reciever):
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class Remote:
    slot: Command = None

    def set_command(self, command):
        Remote.slot = command

    def get_command(self):
        Remote.slot.execute()


if __name__ == '__main__':
    r = Remote()
    light = Light()
    light_on = LightOnCommand(light)
    r.set_command(light_on)
    r.get_command()
