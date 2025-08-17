class Room:
    def __init__(self, name, room_type="normal", description=""):
        self.name = name
        self.description = description
        self.room_type = room_type
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.puzzle = None

    def set_description(self, description):
        self.description = description

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def get_details(self):
        print(f"{self.name}")
        print("-" * 20)
        print(self.description)
        for direction, room in self.linked_rooms.items():
            print(f"The {room.name} is to the {direction}.")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self
    
    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def set_puzzle(self, puzzle):
        self.puzzle = puzzle