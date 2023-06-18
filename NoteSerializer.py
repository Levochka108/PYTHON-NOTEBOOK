from Note import Note


class NoteSerializer:
    @staticmethod
    def serialize(note):
        return {
            "id": note.id,
            "title": note.title,
            "body": note.body,
            "timestamp": note.timestamp
        }
    @staticmethod
    def deserialize(data):
        return Note(
            id=data["id"],
            title=data["title"],
            body=data["body"],
            timestamp=data["timestamp"]
        )