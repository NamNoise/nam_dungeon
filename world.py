from typing import List, Optional

class Puzzle:
    def __init__(self, puzzle_id: str, question: str, answer: str, clue: Optional[str] = None):
        self.puzzle_id = puzzle_id
        self.question = question
        self.answer = answer
        self.clue = clue
        self.solved = False

    def attempt(self, text: str) -> bool:
        if text.strip().lower() == self.answer.strip().lower():
            self.solved = True
            return True
        return False

class StoryEvent:
    def __init__(self, event_id: str, text: str, journal_entry: Optional[str] = None, branch_flag: Optional[str] = None):
        self.event_id = event_id
        self.text = text
        self.journal_entry = journal_entry
        self.branch_flag = branch_flag

class Room:
    def __init__(
        self,
        room_id: str,
        room_type: str,
        description: str,
        connected: Optional[List[str]] = None,
        puzzle: Optional[Puzzle] = None,
        loot: Optional[List[str]] = None,
        event: Optional[StoryEvent] = None,
        has_hidden_path: bool = False,
        hidden_room_id: Optional[str] = None,
        lever_id: Optional[str] = None
    ):
        self.room_id = room_id
        self.room_type = room_type
        self.description = description
        self.connected = connected or []
        self.puzzle = puzzle
        self.loot = loot or []
        self.event = event
        self.has_hidden_path = has_hidden_path
        self.hidden_room_id = hidden_room_id
        self.lever_id = lever_id

    def describe(self, reveal_hidden=False, reveal_condition=False):
        
