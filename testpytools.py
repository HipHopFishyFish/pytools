import pytools.ansipy as ansipy

print("---------- ANSIPY TEST ----------")
print(ansipy.ANSI("fg_col", "red") + "red" + ansipy.RESET)
print(ansipy.ANSI("fg_col", "green") + "green" + ansipy.RESET)
print(ansipy.ANSI("fg_col", "blue") + "blue" + ansipy.RESET)
print()
print(ansipy.ANSI("bg_col", "red") + "red" + ansipy.RESET)
print(ansipy.ANSI("bg_col", "green") + "green" + ansipy.RESET)
print(ansipy.ANSI("bg_col", "blue") + "blue" + ansipy.RESET)
