#!/usr/bin/python3
"""Print all the letters except q and e, not followed by a new line."""
for i in range(97, 123):
    if chr(i) != 'q' and chr(i) != 'e':
        print("{}".format(chr(i)), end="")
