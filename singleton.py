from abc import ABCMeta

class SingleAbstract(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        print("call is called")
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonClass(metaclass=SingleAbstract):
    pass


class CallTest(SingleAbstract):
    def __init__(self):
        pass
    def __call__(cls, *args, **kwargs):
        print("Call test is called")
        return super().__call__(*args, **kwargs)

    def __new__(self , *args, **kwargs):
        return super().__new__(*args, **kwargs)
