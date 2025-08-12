class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item_id):
        self.items = [i for i in self.items if i.item_id != item_id]

    def has(self, item_id):
        return any(i.item_id == item_id for i in self.items)

    def list_names(self):
        return [i.name for i in self.items]

class Player:
    def __init__(self, name="Explorer"):
        self.name = name
        self.current_room_id = None
        self.inventory = Inventory()
        self.journal = []
        self.puzzles_solved = set()
        self.flags = {}
        self.endings_unlocked = []

    def add_journal(self, text):
        if text and text not in self.journal:
            self.journal.append(text)

    def pickup(self, text):
        self.inventory.add(item)

    def use_item(self, item_id):
        if self.inventory.has(item_id):
            return True
        return False


