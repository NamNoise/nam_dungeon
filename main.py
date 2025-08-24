from room import Room
from character import Enemy, Friend, Player
from item import Item
from puzzle import Puzzle
from glassbridge import GlassBridge
import time

'''
This is the main game loop for a text-based adventure game.
Players explore rooms, fight enemies, solve puzzles, collect items, and attempt to escape by crossing a glass bridge to the exit.
'''

# Player initialization
player = Player("Hero", "A brave adventurer exploring the dungeon.")

# Room creation
spawn = Room("Spawnpoint", "A dimly lit stone chamber, cold air flows in from unseen cracks.")
treasure_hall = Room("Treasure Hall", "A glittering hall with chests lining the walls.")
puzzle_room = Room("Puzzle Room", "An ancient room filled with mysterious carvings.", "puzzle")
exit_room = Room("Dungeon Exit", "A massive stone gate stands before you. Freedom lies beyond.", "exit")
glass_bridge = GlassBridge(steps=3)
hidden_room = Room("Hidden Chamber", "A secret chamber filled with ancient treasures.") 

# Link rooms
spawn.link_room(treasure_hall, "north")
treasure_hall.link_room(spawn, "south")
treasure_hall.link_room(puzzle_room, "east")
puzzle_room.link_room(treasure_hall, "west")
puzzle_room.link_room(exit_room, "north") 
puzzle_room.add_hidden_room(hidden_room, "east") # hidden room initially blocked

# Character setup
goblin = Enemy("Goblin", "A small, green, and very grumpy dungeon inhabitant.")
goblin.set_conversation("Grrr... You shall not pass without a fight!")
goblin.set_weakness("sword")
treasure_hall.set_character(goblin)

sage = Friend("Old Sage", "A wise man in ragged robes.")
sage.set_conversation("The walls hide more than they reveal. Solve the puzzle to proceed.")
puzzle_room.set_character(sage)

# Item setup
sword = Item("sword", "A sharp blade, perfect for fending off enemies and close combat.")
spawn.set_item(sword)
ancient_key = Item("ancient key", "An old iron key, looks like it could open a hidden door.")
treasure_hall.set_item(ancient_key)
treasure = Item("golden idol", "An ancient treasure from a hidden chamber.")
hidden_room.set_item(treasure)

# Puzzle setup
riddle = Puzzle("What walks on four legs in the morning, two at noon, and three at night?", "human")
puzzle_room.set_puzzle(riddle)

# Game state variables
current_room = spawn
previous_room = None
dead = False
escaped = False

# Game intro
print("Welcome to the Dungeon Adventure!")
print("Your goal is to escape the dungeon by solving puzzles, fighting enemies, and collecting items.")
print("Type 'exit' to exit at any time, or 'quit' to end the game.")

# Main game loop
while not (dead or escaped):
    print("\n")
    # Show room details and available directions
    current_room.get_details()

    if current_room.name == "Hidden Chamber": # Hidden chamber logic
        print("You step into a hidden chamber. Treasures glitter around you.")
        room_item = current_room.get_item()
        if room_item:
            room_item.describe()
            print("You can type 'take' to grab the treasure.")
        else:
            print("The chamber now stands empty, its treasures already claimed.")

        # Hidden chamber is temporary: player is pushed back automatically        
        command = input("> ").lower().strip()
        if command == "take" and room_item:
            print(f"You take the {room_item.name}.")
            player.take_item(room_item.name)
            current_room.set_item(None)
        elif command == "bag":
            if player.inventory:
                print("You have the following items in your bag:")
                for i in player.inventory:
                    print(f"- {i}")
            else:
                print("Your bag is empty.")
        else:
            print("You hesitate, and the chamber begins to push you back...")
        time.sleep(2)
        print("A mysterious force pushes you back to the Treasure Hall.")
        current_room = previous_room
        continue # Skip the rest of the loop for hidden room

    # Describe character and prompt for interaction   
    inhabitant = current_room.get_character()
    if inhabitant:
        inhabitant.describe()

    # Describe room item and prompt for pickup
    room_item = current_room.get_item()
    if room_item:
        room_item.describe()
        take_choice = input(f" Do you want to take the {room_item.name}? (yes/no): ").lower().strip()
        if take_choice == "yes":
            print(f"You take the {room_item.name}.")
            player.take_item(room_item.name)
            current_room.set_item(None)
        else:
            print(f"You leave the {room_item.name} behind.")

    # Puzzle prompt
    if current_room.room_type == "puzzle" and current_room.puzzle and not current_room.puzzle.solved:
        print("There is a puzzle here, it asks:", current_room.puzzle.question)
        print("You can attempt to solve it by typing 'solve' followed by your answer.")

    # Player command input
    command = input("> ").lower().strip()

    # Movement and action handling
    if command in ["north", "south", "east", "west"]:
        if isinstance(current_room.get_character(), Enemy): # Goblin blocks the path if present
            print(f"The {current_room.get_character().name} blocks your path! You must defeat it first.")
        else:
            next_room = current_room.move(command)
            if next_room:
                previous_room = current_room
                current_room = next_room
                print(f"You move to {current_room.name}.")
                if current_room.linked_rooms:
                    dirs = [d.capitalize() for d in current_room.linked_rooms.keys()]
                    print("You can go: " + (dirs[0] + "." if len(dirs) == 1 else ", ".join(dirs[:-1]) + "and " + dirs[-1] + "."))
                else:
                    print("There are no visible exits.")
                # Show glass bridge description when entering exit room
                if current_room.room_type == "exit":
                    print(glass_bridge.description)
            else:
                print("You can't go that way!")

    # Special commands for exit room
    elif command == "exit":
        current_room = current_room.move(command)
    
    # Talk to a character
    elif command == "talk" and inhabitant:
        inhabitant.talk()

    # Fight an enemy
    elif command == "fight" and isinstance(inhabitant, Enemy): # Check if player type "fight" and if there's a fightable enemy
        print("What will you fight with?")
        fight_with = input("> ").lower().strip() # Player weapon command input
        if fight_with in player.inventory: # Check if weapon in player's inventory
            if inhabitant.fight(fight_with): # Check if the enemy can be defeated with the selected weapon
                print("You defeated the enemy! The path is now clear.")
                current_room.set_character(None)
                # Show new exits after defeating enemy
                if current_room.linked_rooms:
                    dirs = [d.capitalize() for d in current_room.linked_rooms.keys()]
                    # Print available directions after defeating the enemy
                    print("You can go: " + (dirs[0] + "." if len(dirs) == 1 else ", ".join(dirs[:-1]) + " and " + dirs[-1] + "."))
                else: # If no exits in the room, then print the following line
                    print("There are no visible exits.")
            else: # If the item selected is not a weapon, then the enemy will defeat the player
                print("You were defeated...")
                dead = True
        else:
            print("You don't have that item to fight with!")

    # Pat a friendly character
    elif command == "pat" and isinstance(inhabitant, Friend):
        inhabitant.pat()

    # Take an item
    elif command == "take" and room_item: # Check if there's an item in the room when type "take"
        print(f"You take the {room_item.name}.")
        player.take_item(room_item.name) # Add item to inventory
        current_room.set_item(None) # Remove item from room

    # Show inventory
    elif command == "bag": # Check if player types "bag" to see inventory
        if player.inventory: # Check if inventory is not empty
            print("You have the following items in your bag:")
            for i in player.inventory: # Loop through and print each item
                print(f"- {i}")
        elif player.inventory == []: # Handle empty inventory
            print("Your bag is empty.")
    
    # Solve puzzle
    elif command == "solve" and current_room.puzzle: # Check if there's a puzzle in the room when type "solve"
        answer = input("Your answer: ").lower().strip() # Prompt for puzzle answer
        if current_room.puzzle.attempt(answer): # Check if answer fit with puzzle set answer
            print("The puzzle is solved! A path forward is revealed.")
            # Reveal hidden rooms after puzzle
            for direction in list(current_room.hidden_rooms.keys()): # Reveal all hidden rooms
                current_room.reveal_hidden(direction) 
        else: # Incorrect answer handling
            print("Incorrect answer. Try again.")
    
    # Cross the glass bridge
    elif command == "cross bridge" and current_room.room_type == "exit": # Check if the player is at the exit room when type "cross bridge"
        if glass_bridge.completed: # Check if already crossed then print success message
            print("You have already crossed the bridge safely.")
        elif glass_bridge.failed: # Check if already failed then print falling message
            print("The glass shatters beneath you! You fall into the abyss...")
            dead = True # make player dead
        else: # Check if not crossed or failed then start crossing sequence
            print("You step onto the glass bridge...")
            while not (glass_bridge.completed or glass_bridge.failed): # Loop until bridge is crossed or failed
                choice = input("Choose your step (left/right): ").lower().strip() # Prompt for left/right step
                if choice in ["left", "right"]: # Validate input
                    if glass_bridge.attempt_step(choice): # Attempt the step
                        if glass_bridge.completed: # Check if completed after step then print success message
                            print("You crossed the glass bridge safely!")
                        else: # Print safe step message
                            print("Safe! You move forward to the next step...")
                    else: # If step fails, print falling message and mark as failed
                        print("CRACK! The glass shatters beneath you! You fall into the abyss...")
                        glass_bridge.failed = True
                        dead = True
                else: # Invalid input handling
                    print("Invalid choice. You must choose 'left' or 'right'.")
    
    # Open exit door
    elif command == "open exit" and current_room.room_type == "exit":
        if not glass_bridge.completed: # Check if the player has crossed the bridge
            print("You need to cross the glass bridge first before opening the exit!")
        else: # Attempt to open exit
            print("You approach the massive stone gate.")
            if "ancient key" in player.inventory: # Check for key
                print("You have the ancient key. Do you want to use it to open the gate? (yes/no)")
                use_key = input("> ").lower().strip() # Prompt for using key
                if use_key == "yes": # Use the key to open exit
                    print("You insert the ancient key into the lock and turn it. The gate creaks open!")
                    current_room = exit_room
                    print("You step through the gate and into the light of freedom!")
                escaped = True
            else:
                print("The gate is locked. You need an ancient key to open it. Search for it in the dungeon.")
    
    # Quit the game
    elif command == "quit":
        print("Aww, already leaving? Come back with more courage next time!")
        dead = True
    
    # Invalid command handling
    else:
        print("Invalid command. Try one of these:")
        print("- Movement: north, south, east, west")
        print("- Actions: talk (if there's a inhabitant in room), fight (if there's a inhabitant in room), " \
        "pat (if there's), take, bag, solve, open exit")
        print("- Exit: quit")

# End game messages
if escaped:
    print("\nCongratulations! You have escaped the dungeon!")
elif dead:
    print("\nYour journey ends here. Better luck next time!")

print("-" * 20)
print("Thank you for playing!")
print("-" * 20)
print("Game Over. Exiting in 3...")
time.sleep(1) # Pause for dramatic effect
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("-" * 20)
print("Goodbye!")