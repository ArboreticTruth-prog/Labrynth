class Room():
    """Creates the room and its attatchments/exits"""
    def __init__(self):
        """Intializes the attatch/exits"""
        self.left = False
        self.right = False
        self.front = False
        self.back = False
        
    def left_attch(self, x):
        self.left  = x
        

    def right_attch(self, y):
        self.right = y

    def back_attch(self, c):
        self.back = c

    def front_attch(self, f):
        self.front = f
        

    # def print_att(self):
    #     print('left', self.left, 'right', self.right, 'back', self.back, 'front', self.front)