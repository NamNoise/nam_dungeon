import random

class GlassBridge: # Represents a glass bridge that the player must cross at the end of the game
    def __init__(self, steps=3): # Attributes for the glass bridge
        self.steps = steps # steps (int): Number of steps to cross the bridge
        self.current_step = 0 # current_step (int): Current step the player is on
        self.pattern = [random.choice(["left", "right"]) for _ in range(steps)] # pattern (list): Randomly generated safe steps
        self.failed = False # failed (bool): Whether the player has fallen
        self.completed = False # completed (bool): Whether the player has crossed the bridge
        self.description = "A narrow glass bridge stretches across a dark abyss to the exit. Each step looking dangerously fragile." # description (str): Description of the bridge

    def attempt_step(self, choice):
        '''
        Attempt a single step on the glass bridge.

        Args:
            choice (str): "left" or right" chosen by the player.

        Returns:
            bool: True if safe, False if the glass breaks.
        '''
        if self.failed or self.completed:
            return False
        
        safe_side = self.pattern[self.current_step]
        if choice == safe_side:
            self.current_step += 1
            if self.current_step == self.steps:
                self.completed = True
            return True
        else:
            self.failed = True
            return False