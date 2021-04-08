import sys


def print_vars():
    frame = sys._getframe(1)
    for name in frame.f_locals:
        value = frame.f_locals[name]
        is_builtin = value.__class__.__module__ == 'builtins'
        print('{0}: {1}'.format(name, is_builtin))
