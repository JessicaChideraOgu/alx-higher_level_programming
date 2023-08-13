#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    """This prints all the names defined by hidden_4 module."""

module_names = dir(hidden_4)
for name in module_names:
    if name[:2] != "__":
        print(name)
