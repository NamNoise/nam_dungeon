class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def set_description(self, description):
        self.description = description
    
    def get_name(self):
        return self.name

    def describe(self):
        print(f"You see a {self.name} - {self.description}")
    
    def use(self):
        print(f"You use the {self.name}.")
        