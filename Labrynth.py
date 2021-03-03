from trackings import tracking_counts
from room_build import build_room
class game_loop():
    def __init__(self):
        """ 
        initializes specifics for functions

        """
        self.playerm = []
        self.call = build_room()
        self.call.building()
        self.call.built()

    

    def player_move(self):
        """
        prompts users input and diverges it to sepcific functions based on direction

        """
        run = self.call.building()
       
        direction = input("Which way?? ")
        if run == 3 and direction == "left":
            print("Move", direction)
            self.playerm.append(direction)
            print(self.playerm)
            self.call.built()
            return self.player_move()

        elif run == 2 and direction == "right":
            print("Move", direction)
            self.playerm.append(direction)
            print(self.playerm)
            self.call.built()
            return self.player_move()

        elif run == 1 and direction == "front":
            print("Move", direction)
            self.playerm.append(direction)
            print(self.playerm)
            self.call.built()
            return self.player_move()

        elif direction == "back":
            if not self.playerm:
                print("cant go back")
            else:
                self.playerm.pop()
                print(self.call.built())
                return self.player_move() 

        else:
            print("Wall")
            return self.player_move()
            
    def moved(self):
        return self.playerm

test = game_loop()
test.player_move()

