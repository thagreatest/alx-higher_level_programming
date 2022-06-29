#!/usr/bin/python3
"""Print all the letters except q and e, not followed by a new line."""
for a in range(ord('a'), ord('z') + 1):
    if chr(a) != 'e' and chr(a) != 'q':
        print("{:c}".format(a), end='')
