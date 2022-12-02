#!/usr/bin/python3
# 2-args: prints the number of and the list of its arguments.
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
