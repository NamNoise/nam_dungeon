class Character: # Base class for all characters in the game
    def __init__(self, name, description): # Attributes for the character
        self.name = name # name (str): Name of the character
        self.description = description # description (str): Description of the character
        self.conversation = None # conversation (str): Dialogue the character can say

    def set_conversation(self, conversation): # Set the dialogue for the character
        self.conversation = conversation

    def describe(self): # Print description of the character
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self): # Print character's dialogue if set
        if self.conversation:
            print(f"[{self.name} says]: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk right now.")

class Enemy(Character): # Represents an enemy character that can block paths and fight the player
    def __init__(self, name, description): # Attributes for the enemy
        super().__init__(name, description) # Inherit from Character
        self.weakness = None # weakness (str): Item that can defeat the enemy

    def set_weakness(self, weakness): # Set the item that can defeat the enemy
        self.weakness = weakness

    def fight(self, item_name):
        '''
        Attempt to defeat the enemy with a given item.
        Args:
            item_name (str): Name of the item used to fight.
        Returns:
            bool: True if enemy defeated, False otherwise.
        '''
        if item_name.lower() == str(self.weakness).lower():
            print(f"You fend off {self.name} with the {item_name}!")
            return True
        else:
            print(f"{self.name} overpowers you with its strength...")
            return False

class Friend(Character): # Represents a friendly character the player can interact with
    def __init__(self, name, description): 
        super().__init__(name, description) 

    def pat(self): # Print a friendly interaction
        print(f"{self.name} smiles and pats you back.")

class Player(Character): # Represents the player character and their inventory
    def __init__(self, name, description): # Attributes for the player
        super().__init__(name, description) # Inherit from Character
        self.inventory = [] # List of items the player has

    def take_item(self, item): # Add an item to the player's inventory
        self.inventory.append(item)
        print(f"You added {item} to your bag.")

    def show_inventory(self): # Print all items in player's inventory
        print("You have the following items in your bag:")
        if self.inventory:
            for it in self.inventory:
                print(f"- {it.name}")
        else:
            print("Your bag is empty.")

    def has_item(self, item_name): # Check if player has an item by name
        return any(it.name.lower() == item_name.lower() for it in self.inventory)

    def fight_enemy(self, enemy, item_name):
        '''
        Attempt to fight an enemy using an item in inventory.
        Returns True if successful, False otherwise.
        '''
        for it in self.inventory:
            if it.name.lower() == item_name.lower():
                return enemy.fight(it.name.lower())
        print("You don't have that item to fight with!") 