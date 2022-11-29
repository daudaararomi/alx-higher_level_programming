#!/usr/bin/python3
# Print the alphabet in lowercase except q and e, not followed by a new line.
for alphabet in range(97, 123):
    if chr(alphabet) == "e":
        continue
    elif chr(alphabet) == "q":
        continue
    else:
        print("{}".format(chr(alphabet)), end="")
