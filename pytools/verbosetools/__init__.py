import datetime


def now():
    return datetime.datetime.now().strftime("%H:%M:%S")

class _Verbose:
    def __init__(self, klass, **kwargs):
        if kwargs.get("level", None) == None:
            kwargs["level"] = 1

        if kwargs.get("msg_format", None) == None:
            kwargs["msg_format"] = "[%s]: %s"

        self.klass = klass
        self.level = kwargs["level"]
        self.msg_format = kwargs["msg_format"]

    def push_verbose(self, msg, level=1):
        if self.level >= level:
            print(self.msg_format % (now(), msg))


def Verbose(klass=None, **kwargs):
    if kwargs == {}:
        def inner(*args, **kwargs):
            nonlocal klass
            klass.verbose = _Verbose(klass)
            klass(*args, **kwargs)
    else:
        def inner(klass):
            def inner_():
                klass.verbose = _Verbose(klass, **kwargs)

            return inner_


    return inner