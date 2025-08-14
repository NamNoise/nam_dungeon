class Puzzle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer.lower()
        self.solved = False
    
    def attempt(self, guess):
        if guess == self.answer:
            self.solved = True
            print("Correct! The puzzle is solved.")
            return True
        return False