class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = None

    def set_conversation(self, conversation):
        self.conversation = conversation

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        if self.conversation:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk right now.")

class Enemy(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def fight(self, item):
        if item == self.weakness:
            print(f"You fend off {self.name} with the {item}!")
            return True
        else:
            print(f"{self.name} overpowers you with its strength...")
            return False

class Friend(Character):
    def __init__(self, name, description):
        super().__init__(name, description)

    def pat(self):
        print(f"{self.name} smiles and pats you back.")

class Player(Character):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.inventory = []

    def add_to_inventory(self, item_name):
        self.inventory.append(item_name)
        print(f"{item_name} has been added to your inventory.")

    def move_to(self, room):
        print(f"You move to {room.name}.")
        return room

        
        