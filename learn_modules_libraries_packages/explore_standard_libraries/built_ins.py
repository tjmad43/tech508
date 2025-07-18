# module for finding out what modules are built in
import builtins

for name in dir(builtins):
    if name[0].islower():
        print(name)