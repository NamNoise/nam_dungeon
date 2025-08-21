from room import Room
from character import Enemy, Friend, Player
from item import Item
from puzzle import Puzzle
import time

# --- Create rooms ---
spawn = Room("Spawnpoint", description="A dimly lit stone chamber, cold air flows in from unseen cracks.")
treasure_hall = Room("Treasure Hall", description="A glittering hall with chests lining the walls.")
puzzle_room = Room("Puzzle Room", description="An ancient room filled with mysterious carvings.")
exit_room = Room("Dungeon Exit", description="A massive stone gate stands before you. Freedom lies beyond.", room_type="exit")

# Link rooms
spawn.link_room(treasure_hall, "north")
treasure_hall.link_room(spawn, "south")
treasure_hall.link_room(puzzle_room, "east")
puzzle_room.link_room(treasure_hall, "west")
puzzle_room.link_room(exit_room, "north")

# --- Create characters ---
goblin = Enemy("Goblin", "A small, green, and very grumpy dungeon inhabitant.")
goblin.set_conversation("Grrr... You shall not pass without a fight!")
goblin.set_weakness("sword")
treasure_hall.set_character(goblin)

sage = Friend("Old Sage", "A wise man in ragged robes.")
sage.set_conversation("The walls hide more than they reveal. Solve the puzzle to proceed.")
puzzle_room.set_character(sage)

# --- Create items ---
sword = Item("sword", "A sharp blade, perfect for fending off enemies and close combat.")
spawn.set_item(sword)

key = Item("ancient key", "An old iron key, looks like it could open a hidden door.")
treasure_hall.set_item(key)

# --- Create puzzle ---
riddle = Puzzle("What walks on four legs in the morning, two at noon, and three at night?", "human")
puzzle_room.set_puzzle(riddle)

# --- Create player ---
player = Player("Hero", "The brave adventurer.")
current_room = spawn
dead = False
escaped = False

# --- Game Loop ---
while not (dead or escaped):
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant:
        inhabitant.describe()

    item = current_room.get_item()
    if item:
        item.describe()

    if current_room.puzzle and not current_room.puzzle.solved:
        print("There is a puzzle here. Type 'solve' to attempt it.")

    command = input("> ").lower().strip()

    # --- Movement ---
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    # --- Talk ---
    elif command == "talk" and inhabitant:
        inhabitant.talk()

    # --- Fight ---
    elif command == "fight" and isinstance(inhabitant, Enemy):
        print("What will you fight with?")
        fight_with = input("> ").lower().strip()
        if player.fight_enemy(inhabitant, fight_with):
            current_room.set_character(None)
        else:
            dead = True

    # --- Pat a friend ---
    elif command == "pat" and isinstance(inhabitant, Friend):
        inhabitant.pat()

    # --- Take item ---
    elif command == "take" and item:
        player.take_item(item)
        current_room.set_item(None)

    # --- Show inventory ---
    elif command == "bag":
        player.show_inventory()

    # --- Solve puzzle ---
    elif command == "solve" and current_room.puzzle:
        print(current_room.puzzle.question)
        answer = input("Your answer: ").lower().strip()
        if current_room.puzzle.attempt(answer):
            print("The puzzle is solved! A path forward is revealed.")
        else:
            print("Incorrect answer. Try again.")

    # --- Exit room ---
    elif command == "open exit" and current_room.room_type == "exit":
        print("You approach the massive stone gate.")
        if player.has_item("ancient key"):
            print("You unlock the massive stone gate and step into freedom!")
            escaped = True
        else:
            print("The gate is locked. You need a key to open it.")

    # --- Quit game ---
    elif command == "quit":
        print("Aww, already leaving? Come back with more courage next time!")
        dead = True

    else:
        print("Invalid command. Try 'north', 'south', 'east', 'west', 'talk', 'fight', 'pat', 'take', 'bag', 'solve', or 'open exit'.")

# --- End game ---
if escaped:
    print("\nCongratulations! You have escaped the dungeon!")
elif dead:
    print("\nYour journey ends here. Better luck next time!")
print("Thank you for playing!")

time.sleep(2)
print("Goodbye!")