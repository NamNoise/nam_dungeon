import random

class GlassBridge:
    def __init__(self, steps=5):
        self.steps = steps
        self.current_step = 0
        self.pattern = [random.choice(["left", "right"]) for _ in range(steps)]
        self.failed = False
        self.completed = False

    def attempt_step(self, choice):
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