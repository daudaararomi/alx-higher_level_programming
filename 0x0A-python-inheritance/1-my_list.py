#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """Contains list
    """
    def __init__(self):
        """ initializes new MyList object """
        pass

    def print_sorted(self):
        """Prints self in sorted format
        """

        print(sorted(self))
