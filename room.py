class Room: # Represents a room in the dungeon
    def __init__(self, name, description, room_type="normal"): # Attributes for the room
        self.name = name # name (str): Name of the room
        self.description = description # description (str): Description of the room
        self.room_type = room_type # room_type (str): Type of the room, e.g., "normal", "puzzle", "exit"
        self.linked_rooms = {} # linked_rooms (dict): rooms connected to this room in each direction
        self.hidden_rooms = {} # hidden_rooms (dict): hidden rooms that can be revealed later
        self.character = None # character (Character): Enemy, or Friend present in the room
        self.item = None # item (Item): Item present in the room
        self.puzzle = None #puzzle (Puzzle): Puzzle present in the room

    def set_description(self, description): # Set or update the room's description
        self.description = description 

    def set_character(self, character): # Place a character (Enemy or Friend) in the room
        self.character = character
    
    def get_character(self): # Return the character currently in the room, if any
        return self.character

    def set_item(self, item): # Place an item in the room
        self.item = item
        
    def get_item(self): # Return the item currently in the room, if any
        return self.item

    def link_room(self, room, direction):
        '''
        Connect another room to this one in the given direction.
        
        Args:
            room (Room): Room object to link.
            direction (str): "north", "south", "east", or "west".
        '''
        self.linked_rooms[direction] = room

    def get_details(self): # Print the room's details, including description and available directions
        print(f"{self.name}")
        print("-" * 20)
        print(self.description)
        
        # Display linked rooms/exits in readable format
        if self.linked_rooms:
            directions = [direction.capitalize() for direction in self.linked_rooms.keys()]
            if len(directions) == 1:
                print(f"You can go {directions[0]} (type out the direction).")
            else:
                print("You can go: " + ", ".join(directions[:-1]) + " and " + directions[-1] + " (type out the direction).")
        else:
            print("There are no visible exits.")


    def move(self, direction):
        '''
        Return the room in the chosen direction, if it exists.
        Args:
            direction (str): Direction player wants to move.
        Returns:
            Room or None
        '''
        return self.linked_rooms.get(direction, None)

    def set_puzzle(self, puzzle): # Assign a puzzle to the room
        self.puzzle = puzzle

    def add_hidden_room(self, room, direction): # Add a hidden room that can later be revealed
        self.hidden_rooms[direction] = room
    
    def reveal_hidden(self, direction): # Reveal a hidden room in the given direction
        if direction in self.hidden_rooms:
            self.linked_rooms[direction] = self.hidden_rooms.pop(direction)
            print(f"A hidden path to the {direction} is revealed!")
            print("You can now move in that direction.")
        else:
            print(f"No hidden room in the {direction} direction.") 