from roombuilder import mass_gen


## this is just a test to see if I can push code
class game_loop():
    """Runs the game"""
    def __init__(self):
        self.call = mass_gen()

    def input_loop(self):
        """ Loops until user enters valid move """
        print('Enter Direction')
        user_move = input()
        # checks if they enter proper move
        if user_move in ['forward','backward','left','right']:
            return user_move
        # if they dont then it asks again
        else:
            return self.input_loop()

    def room_loop(self):
        """ Loops until user exits room """
        user_move = self.input_loop()
        if self.call.can_move(user_move):
            return True
        else: 
            return self.room_loop

    def run(self):
        print('welcome')
        # makes the base room
        self.call.next_room('first')
        while True:
            self.room_loop()

test = game_loop()
test.run()