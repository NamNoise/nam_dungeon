class Room:
    def __init__(self, name, room_type="normal", description=""):
        self.name = name
        self.description = description
        self.room_type = room_type
        self.linked_rooms = {}
        self.hidden_rooms = {}
        self.character = None
        self.item = None
        self.puzzle = None

    def set_description(self, description):
        self.description = description

    def set_character(self, character):
        self.character = character
    
    def get_character(self):
        return self.character

    def set_item(self, item):
        self.item = item

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def get_details(self):
        print(f"{self.name}")
        print("-" * 20)
        print(self.description)
        
        if self.linked_rooms:
            exits = ", ".join(self.linked_rooms.keys())
            print(f"Exits: {exits}")
        else:
            print("There's no obvious way out here.")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self

    def get_item(self):
        return self.item

    def set_puzzle(self, puzzle):
        self.puzzle = puzzle

    def add_hidden_room(self, room, direction):
        self.hidden_rooms[direction] = room
    
    def reveal_hidden(self, direction):
        if direction in self.hidden_rooms:
            self.hidden_room[direction] = self.hidden_rooms.pop(direction)
            print(f"A hidden path to the {direction} is revealed!")