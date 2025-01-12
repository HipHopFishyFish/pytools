_fg_colours = {
    "BLACK": "0m",
    "RED": "1m",
    "GREEN": "40m",
    "YELLOW": "3m",
    "BLUE": "6m",
    "MAGENTA": "5m",
    "CYAN": "3m",
    "WHITE": "7m"
}

_bg_colours = {
    "BLACK": "40m",
    "RED": "41m",
    "GREEN": "42m",
    "YELLOW": "43m",
    "BLUE": "44m",
    "MAGENTA": "45m",
    "CYAN": "46m",
    "WHITE": "47m"
}

def can_be_int(num):
    try:
        int(num)
        return True
    except:
        return False

class ANSI:
    def __init__(self, type_, *args):
        if type_ == "reset":
            self.before = "\033["
            self.col_code = "0m"
        if type_ == "fg_col":
            if can_be_int(args[0]) or type(args[0]) == int:
                self.before = "\033[38;5;"
                self.col_code = str(args[0]) + "m"

            elif args[0].upper() in _fg_colours:
                self.before = "\033[38;5;"
                self.col_code = _fg_colours[args[0].upper()]

        if type_ == "bg_col":
            if can_be_int(args[0]) or type(args[0]) == int:
                self.before = "\033[48;5;"
                self.col_code = str(args[0]) + "m"
            elif args[0].upper() in _bg_colours:
                self.before = "\033[48;5;"
                self.col_code = _fg_colours[args[0].upper()]


    def __str__(self):
        return f"{self.before}{self.col_code}"

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)
    

RESET = str(ANSI("reset"))