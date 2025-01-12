import datetime

log_file = ""

def set_log_file(name):
    global log_file
    log_file = name


def now():
    return datetime.datetime.now().strftime("%H:%M:%S")

class _Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        self._start_logging(*args, **kwargs)

    def _start_logging(self, *args, **kwargs):
        try:
            self.func(*args, **kwargs)
        except Exception as e:
            self.log_data(e)
            raise

    def log_data(self, e):
        exception_name = type(e).__name__
        exception_value = str(e)
        exep_str = f"[{now()}]: {exception_name}: {exception_value}\n"

        if log_file != "":
            with open(log_file, "a") as file: file.write(exep_str)
        


def Logger(func):
    log = _Logger(func)

    return log