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

    def fight(self, item_name):
        if item_name.lower() == str(self.weakness).lower():
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

    def add_to_inventory(self, item_obj):
        self.inventory.append(item_obj)
        print(f"{item_obj.name} has been added to your inventory.")

    def has_item(self, name):
        name = name.lower()
        return any(it.get.name().lower() == name for it in self.inventory)

    def move_to(self, room):
        print(f"You move to {room.name}.")
        return room

    def list_inventory(self):
        if not self.inventory:
            print("Your bag is empty.")
            return
        print("You have the following items in your bag:")
        for it in self.inventory:
            print(f"- {it.name}: {it.description}")     