from room_setup import room_setup
import random
""" each room will be its own list of lists
Row 2 = [Room #]
Row 1 = [directions (Ones youve used)]
each direction will be within col 1 to 3 (Left, Right, Front)
back will always be able to lead you back to the previous room
back will need to bring out the previous room, while saving that room to that specific direction
grid will tell you where you have been
grid will also save the rooms to each area (Example: Room 1 will be at center(Row 1, Col 1))
"""


class build_room():
    def __init__(self):
        self.room = []
        
    # def random(self):
    #     """ 
    #     sets the random values for exits in rooms
    #     """
    #     return random.randint(1, 3) 

    def building(self):
        
        rant = random.randint(1,3)
        if rant == 1:
            self.room.append("front")
            return 1
        if rant == 2:
            self.room.append("right")
            return 2
        if rant == 3:
            self.room.append("left")
            return 3
        else: 
            
            pass


    def built(self, row = 1, col = 3):
        if self.room == "front":
            for _ in range(col(1)):
                print("Room", self.room)
        elif self.room == "left":
            for _ in range(col(3)):
                print("Room", self.room)
        elif self.room == "right":
            for _ in range(col(2)):
                print("Room", self.room)
        else:
            print(self.room)

        
