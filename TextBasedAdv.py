import random

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

class mass_gen():
    """Generates the room and its subsequent attatchments"""
    def __init__(self):
        self.player_move = []
        self.count = 0
        self.left_count = 0
        self.right_count = 0
        self.front_count = 0
        self.back_count = 0
    
    def print_counts(self):
        """Prints counts"""
        return print(self.left_count, self.right_count, self.back_count, self.front_count)
    
    def move_room(self):
        """Keeps the player direction/move"""
        return self.player_move
    
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
        
    def counts(self):
        """Keeps track of each direction/exit per room"""
        """self.player_move is a list, these are trying to pull it as a string"""
        print("Here at Counts")
        if self.player_move[-1] == ['left']:
            self.left_count += 1
        elif self.player_move == 'right':
            self.right_count += 1
        elif self.player_move == 'front':
            self.front_count += 1
        elif self.player_move == 'back':
            self.back_count += 1
        else:
            pass

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


class game_loop():
    """Runs the game"""
    def __init__(self):
        self.call = mass_gen()
        self.call.print_counts()
        self.p_m = self.call.move_room()
        # self.exist = self.call.existing_room()
        self.call.new_room() 
        self.call.counts

    def new_room(self):
        """Generates the new room in the game loop"""
        return self.call.new_room() 

    
        
    
    def user_input(self):
        """Calls the user's input and allows for movement through exits"""
        direction =  input("What Direction? ")
        if direction == "left": 
            if self.new_room().left:
                print("Moves", direction)
                self.p_m.append(direction)
                return self.new_room(), self.call.counts
            else:
                print("Wall")
                return self.user_input()
        elif direction == "right":
            if self.new_room().right:
                print("Moves", direction)
                self.p_m.append(direction)
                return self.count and self.new_room()
            else:
                print("Wall")
                return self.user_input()

        elif direction == "front": 
            if self.new_room().front:
                print("Moves", direction)
                self.p_m.append(direction)
                return self.count() and self.new_room()
            else:
                print("Wall")
                return self.user_input()
     
        elif direction == "back": 
            if self.new_room().back:
                print("Moves", direction)
                self.p_m.append(direction)
                return self.count() and self.new_room()
            else:
                print("Wall")
                return self.user_input()

        else:
            print("Bad Input") 
            return self.user_input()

    # def print_moves(self):
    #     print(self.movement)
    
    def export_list(self):
        """exports the list of players moves"""
        print("Here exprt_list")
        return self.movement

    
    
# class player_loop():
#     def __init__(self, row = 0, col = 0):
#         leaf = game_loop()
#         self.move = leaf.export_list()
#         print(self.move)
#         self.col = col
#         self.row = row
#         self.board = []

#     def start(self, player_start):
#         self.player_start = (self.col[1], self.row[0])

#     def place_piece (self):
#         print(self.move)
#         if self.move == ['left']:
#             print ("here place piece")
            

            

             
test = mass_gen()
test1 = game_loop()
test1.user_input()
