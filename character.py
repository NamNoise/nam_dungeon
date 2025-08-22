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
            print(f"You fend off {self.name} with the {item_name}!")
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

    def take_item(self, item):
        self.inventory.append(item)
        print(f"You added {item} to your bag.")

    def show_inventory(self):
        print("You have the following items in your bag:")
        if self.inventory:
            for it in self.inventory:
                print(f"- {it.name}")
        else:
            print("Your bag is empty.")

    def has_item(self, item_name):
        return any(it.name.lower() == item_name.lower() for it in self.inventory)

    def fight_enemy(self, enemy, item_name):
        for it in self.inventory:
            if it.name.lower() == item_name.lower():
                return enemy.fight(it.name.lower())
        print("You don't have that item to fight with!") 