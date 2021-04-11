import sys

import numpy as np


class MyClass:
    def __init__(self):
        pass


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    d = np.array([1, 2, 3])
    print_vars()


def print_vars():
    frame = sys._getframe(1)
    for name in frame.f_locals:
        value = frame.f_locals[name]
        is_builtin = value.__class__.__module__ == 'builtins'
        print('{0}: {1}'.format(name, is_builtin))


if __name__ == "__main__":
    foo()
