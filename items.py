class Item:
    def __init__(self, item_id, name, item_type="misc", effect=""):
        self.item_id = item_id
        self.name = name
        self.item_type = item_type
        self.effect = effect

    def __repr__(self):
        return f"<Item {self.item_id}:{self.name}>"