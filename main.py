from room import Room
from character import Enemy, Friend
from item import Item
from puzzle import Puzzle

spawn = Room("Spawnpoint", "A dimly lit stone chamber, cold air flows in from unseen cracks.")
treasure_hall = Room("Treasure Hall", "A glittering hall with chests lining the walls.", room_type="loot")
puzzle_room = Room("Puzzle Room", "An ancient room filled with mysterious carvings.", room_type="puzzle")
exit_room = Room("Dungeon Exit", "A massive stone gate stands before you. Freedom lies beyond.", room_type="exit")

spawn.link_room(treasure_hall, "north")
treasure_hall.link_room(spawn, "south")
treasure_hall.link_room(puzzle_room, "east")
puzzle_room.link_room(treasure_hall, "west")
puzzle_room.link_room(exit_room, "north")

goblin = Enemy("Goblin", "A small, green, and very grumpy dungeon inhabitant.")
goblin.set_conversation("Grrr... You shall not pass without a fight!")
goblin.set_weakness("sword")
treasure_hall.set_character(goblin)

sage = Friend("Old Sage", "A wise man in ragged robes.")
sage.set_conversation("The walls hide more than they reveal. Solve the puzzle to proceed.")
puzzle_room.set_character(sage)

sword = Item("sword", "A sharp blade, perfect for fending off enemies and close combat.")
spawn.set_item(sword)

key = Item("ancient key", "An old iron key, looks like it could open a hidden door.")
treasure_hall.set_item(key)

riddle = Puzzle("What walks on four legs in the morning, two at noon, and three at night?", "human")
puzzle_room.set_puzzle(riddle)

bag = []
current_room = spawn
dead = False
escaped = False

while not (dead or escaped):
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant:
        inhabitant.describe()

    item = current_room.get_item()
    if item:
        item.describe()

    if current_room.room_type == "puzzle" and current_room.puzzle and not current_room.puzzle.solved:
        print("There is a puzzle here. Type 'solve' to attempt it.")

    command = input("> ").lower().strip()

    if command == "exit":
        current_room = current_room.move(command)
    
    elif command == "talk" and inhabitant:
        inhabitant.talk()

    elif command == "fight" and isinstance(inhabitant, Enemy):
        print("What will you fight with?")
        fight_with = input("> ").lower().strip()
        if fight_with in bag:
            if inhabitant.fight(fight_with):
                print("You deafeated the enemy!")
                current_room.set_character(None)
            else:
                print("You were defeated...")
                dead = True
        else:
            print("You don't have that item to fight with!")

    elif command == "pat" and isinstance(inhabitant, Friend):
        inhabitant.pat()

    elif command == "take" and item:
        print(f"You take the {item.name}.")
        bag.append(item.name)
        current_room.set_item(None)

    elif command == "bag":
        print("You have the following items in your bag:")
        if bag:
            for item in bag:
                print(f"- {item}")
        else:
            print("Your bag is empty.")
    
    elif command == "solve" and current_room.puzzle:
        answer = input("Your answer: ").lower().strip()
        if current_room.puzzle.attempt(answer):
            print("The puzzle is solved! A path forward is revealed.")
        else:
            print("Incorrect answer. Try again.")
    
    elif command == "open exit" and current_room.room_type = "exit":
        print("You approach the massive stone gate.")
        if "ancient key" in bag:
            print("You unlock the massive stone gate and step into freedom!")
            escaped = True
        else:
            print("The gate is locked. You need a key to open it.")
    
    elif command == "quit":
        print("Aww, already leaving? Come back with more courage next time!")
        dead = True
    
    else:
        print("Invalid command. Try 'exit', 'talk', 'fight', 'pat', 'take', 'bag', 'solve', or 'open exit'.")

if escaped:
    print("\nCongratulations! You have escaped the dungeon!")
elif dead:
    print("\nYour journey ends here. Better luck next time!")
print("Thank you for playing!")
import random
import time
print("Game Over. Exiting in 3 seconds...")
time.sleep(3)
print("Goodbye!")