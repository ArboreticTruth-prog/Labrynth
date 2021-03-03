class Room():
    """Creates the room and its attatchments/exits"""
    def __init__(self):
        """Intializes the attatch/exits"""
        self.left = False
        self.right = False
        self.front = False
        self.back = False
        
    def left_attch(self, x):
        """ Adds pointer
        
        args:
            x: object to attach
        """
        self.left  = x

    def right_attch(self, y):
        """ Adds pointer
        
        args:
            y: object to attach
        """
        self.right = y

    def back_attch(self, c):
        """ Adds pointer
        
        args:
            c: object to attach
        """
        self.back = c

    def front_attch(self, f):
        """ Adds pointer
        
        args:
            f: object to attach
        """
        self.front = f

    def return_directions(self):
        """ Returns all directions the room has """
        ret = []
        if self.front:
            ret.append('forward')
        if self.back:
            ret.append('backward')
        if self.left:
            ret.append('left')
        if self.right:
            ret.append('right')
        return ret

