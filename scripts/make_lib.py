from os import listdir, system
from sys import path as spath


def errexit():
    print("Compilation error, exiting")
    exit(1)


spath.append("./submodules/CircuitMPY/")
import circuitmpy

circuitmpy.fetch_mpy()

try:
    print(f"virtUART.py -> virtUART.mpy")
    circuitmpy.compile_mpy("./src/virtUART.py", "./files/virtUART.mpy")
except:
    errexit()

print()
