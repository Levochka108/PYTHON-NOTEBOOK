import json
import os.path
from NoteSerializer import NoteSerializer


class NoteRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            data = json.load(file)
            return [NoteSerializer.deserialize(item) for item in data]

    def save_notes(self, notes):
        data = [NoteSerializer.serialize(note) for note in notes]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)