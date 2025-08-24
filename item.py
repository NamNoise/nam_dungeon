class Item: # Represents an item that can be found in rooms and taken by the player
    def __init__(self, name, description): # Attributes for the item
        self.name = name # name (str): Name of the item
        self.description = description # description (str): Description of the item

    def set_description(self, description): # Set or update the item's description
        self.description = description
    
    def get_name(self): # Return the item's name
        return self.name

    def describe(self): # Print the item's details
        print(f"You see a {self.name} - {self.description}")
        