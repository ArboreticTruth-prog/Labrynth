from roombuilder import mass_gen
from Room import Room

class game_loop():
    """Runs the game"""
    def __init__(self, mass_gen, Room):
        self.call = mass_gen()
        self.call.print_counts()
        self.call.new_room() 
        self.call.left_c
        self.past_rooms = []

    def new_room(self):
        """Generates the new room in the game loop"""
        return self.call.new_room() 

    def user_input(self):
        """Calls the user's input and allows for movement through exits"""
        direction =  input("What Direction? ")
        if direction == "left": 
            if self.new_room().left:
                print("Moves", direction)
                self.past_rooms.append(direction)
                return  self.call.left_c, print(self.past_rooms)
                # self.new_room(),
            else:
                print("Wall")
                return self.user_input()
        elif direction == "right":
            if self.new_room().right:
                print("Moves", direction)
                self.past_rooms.append(direction)
                return self.count and self.new_room()
            else:
                print("Wall")
                return self.user_input()

        elif direction == "front": 
            if self.new_room().front:
                print("Moves", direction)
                # self.p_m.append(direction)
                return self.count() and self.new_room()
            else:
                print("Wall")
                return self.user_input()
     
        elif direction == "back": 
            if self.new_room().back:
                print("Moves", direction)
                # self.p_m.append(direction)
                return self.count() and self.new_room()
            else:
                print("Wall")
                return self.user_input()

        else:
            print("Bad Input") 
            return self.user_input()

    
    # def capture_past_rooms(self):
    #     """Captures and adds players move to list"""
    #     print("here at capture rooms")
    #     player = self.user_input()
    #     player.append(self.past_rooms)
    #     return print(self.past_rooms)