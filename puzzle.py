class Puzzle: # Represents a puzzle that can be solved in a room
    def __init__(self, question, answer): # Attributes for the puzzle
        self.question = question # question (str): The puzzle question text
        self.answer = answer.lower() # answer (str): Correct answer (lowercased for consistency)
        self.solved = False # solved (bool): Whether puzzle has been solved
    
    def attempt(self, guess):
        '''
        Attempt  to solve the puzzle

        Args:
            guess (str): Player's answer
        
        Returns:
            bool: True if correct, False otherwise.
        '''
        if guess == self.answer:
            self.solved = True
            print("Correct! The puzzle is solved.")
            return True
        return False