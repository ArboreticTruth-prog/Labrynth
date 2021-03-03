from Room import Room
import random

class mass_gen():
    """Generates the room and its subsequent attatchments"""
    def __init__(self):
        self.count = 0
        self.start_room = None
        self.current_room = None
    
    def random(self):
        """gen's a random number to use"""
        return random.randint(1, 4)
    
    def new_room(self):
        """Generates a room object
        """
        return Room()
        
    def ran_direction(self,room):
        """generates random direction for room
        
        args: 
            room: the room object to generate for

        return: room object 
        """
        ran_dirt = self.random()
        if 1 == ran_dirt: 
            room.front_attch(True)
        elif 2 == ran_dirt: 
            room.back_attch(True)
        elif 3 == ran_dirt: 
            room.left_attch(True)
        elif 4 == ran_dirt: 
            room.right_attch(True)
        return room

    def ran_exts(self, room):
        """Generates the random number of exits for room 
        
        args: 
            room: the room object 

        returns: room object
        """
        for _ in range(self.random()):
            room = self.ran_direction(room)
        return room
        
    def build_room(self):
        """Generates a new room with exits"""
        room = self.new_room()
        return self.ran_exts(room)

    def next_room(self,direction):
        """ Generates the next room to move into
        
            if no start room or current room 
                sets those

            returns: None if this is first room 
                    else return True
            
        """
        if self.start_room == None:
            self.start_room = self.build_room()
            self.current_room = self.start_room
            return None
        next_gen_room = self.build_room()
        self.attach_rooms(next_gen_room,direction)
        return True

    def attach_rooms(self,room, direction):
        """ Attaches room to current_room then updates current_room to the new room
        
        args: 
            room: room object to add on
        direction: 
            the side to attach room on
                accepts: [front,left,right,back]
        """
        if direction == 'forward':
            # attach new room to current
            self.current_room.front_attch(room)
            # attach current to new
            room.back_attch(self.current_room)
        elif direction == 'left':
            self.current_room.left_attch(room)
            room.right_attch(self.current_room)
        elif direction == 'right':
            self.current_room.right_attch(room)
            room.left_attch(self.current_room)
        elif direction == 'backward':
            self.current_room.back_attch(room)
            room.front_attch(self.current_room)
        else: 
            return None
        # make current room the new room
        self.current_room = room

    def can_move(self,direction):
        """ Checks if current room has exit
            makes next room if exit
        
        args: 
            direction: the side of room to check for exit

        return: bool if able to move
        """
        if direction in self.current_room.return_directions():
            print('move into the next room')
            # makes next room 
            self.next_room(direction)
            return True
        else:
            print("Can't move that way")
            return False