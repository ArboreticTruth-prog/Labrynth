from room import Room
import random
class mass_gen():
    """Generates the room and its subsequent attatchments"""
    def __init__(self):
        self.count = 0
        self.left_count = 0
        self.right_count = 0
        self.front_count = 0
        self.back_count = 0
    
    def print_counts(self):
        """Prints counts"""
        return print(self.left_count, self.right_count, self.back_count, self.front_count)
    
    
    def random(self):
        """gen's a random number to use"""
        return random.randint(1, 4)
    
    def random_room(self):
        """Builds the room"""
        # names = ["bed1", "bed2", "bed3",'bed4' ]
        # ran_gen = self.random()
        self.room_built = Room()
            
        
        
    def ran_direction(self):
        """generates random directions for each room"""
        room = self.room_built
        ran_dirt = self.random()
        if 1 == ran_dirt: 
            room.front_attch(True)
        elif 2 == ran_dirt: 
            room.back_attch(True)
        elif 3 == ran_dirt: 
            room.left_attch(True)
        elif 4 == ran_dirt: 
            room.right_attch(True)
        self.count += 1
        self.room_built = room
        
    def left_c(self):
        """Tracks left movement"""
        print("at left count")
        self.left_count += 1
    # def counts(self):
    #     """Keeps track of each direction/exit per room"""
    #     """self.player_move is a list, these are trying to pull it as a string"""
    #     print("Here at Counts")
    #     if ['left']:
    #         self.left_count += 1
    #         print(self.left_count)
    #     elif self.player_move == 'right':
    #         self.right_count += 1
    #     elif self.player_move == 'front':
    #         self.front_count += 1
    #     elif self.player_move == 'back':
    #         self.back_count += 1
    #     else:
    #         pass

        # if self.left_count >= 1:
        #     "+".join(self.player_move)
        #     print(self.player_move)
        #     return self.ran_exts(), self.new_room()
        #     # return self.ran_exts(), self.room_built
        # if self.right_count >= 1:
        #     self.right_count.join(self.player_move)
        #     print(self.player_move)
        #     self.ran_exts()
        #     return self.room_built
        # elif self.front_count >= 1:
        #     self.front_count.join(self.player_move)
        #     print(self.player_move)
        #     self.ran_exts()
        #     return self.room_built
        # elif self.back_count >= 1:
        #     self.player_move.remove("back")
        #     Add = self.player_move.pop(-1)
        #     Add.join(self.room_built)
        #     return self.room_built 
        # else:
        #     return self.new_room

    def ran_exts(self):
        """Generates the random directions/exits"""
        # print("here at ran_exts")
        x = self.random()
        for _ in range(x):
            self.ran_direction()
        # for i in range(exits):
        #     self.ran_direction()
        
        
    # def existing_room(self):
    #     """Will keep track of the rooms already passed through"""
        
    #     if self.left_count >= 1:
    #         self.left_count.join(self.player_move)
    #         print(self.player_move)
    #         return self.room_built
    #     elif self.right_count >= 1:
    #         self.right_count.join(self.player_move)
    #         print(self.player_move)
    #         self.ran_exts()
    #         return self.room_built
    #     elif self.front_count >= 1:
    #         self.front_count.join(self.player_move)
    #         print(self.player_move)
    #         self.ran_exts()
    #         return self.room_built
    #     elif self.back_count >= 1:
    #         self.player_move.remove("back")
    #         Add = self.player_move.pop(-1)
    #         Add.join(self.room_built)
    #         return self.room_built 
    #     else:
    #         return self.new_room
        
        

    def new_room(self):
        """Generates the new_room when moving through an exit"""
        self.random_room()
        self.ran_exts()
        return self.room_built
