class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_description(self, description):
        self.description = description
    
    def get_name(self):
        return self.name

    def describe(self):
        print(f"You see a {self.name} - {self.description}")
        