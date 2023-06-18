import datetime

from Note import Note


class NoteManager:
    def __init__(self, note_repository):
        self.note_repository = note_repository

    def add_note(self, title, body):
        notes = self.note_repository.load_notes()
        note_id = str(len(notes) + 1)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(note_id, title, body, timestamp)
        notes.append(note)
        self.note_repository.save_notes(notes)
        print("Заметка добавлена.")

    def edit_note(self, note_id, new_title, new_body):
        notes = self.note_repository.load_notes()
        note = next((n for n in notes if n.id == note_id), None)
        if note:
            if new_title:
                note.title = new_title
            if new_body:
                note.body = new_body
            note.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.note_repository.save_notes(notes)
            print("Заметка отредактирована.")
        else:
            print("Заметка с указанным ID не найдена.")

    def delete_note(self, note_id):
        notes = self.note_repository.load_notes()
        note = next((n for n in notes if n.id == note_id), None)
        if note:
            notes.remove(note)
            self.note_repository.save_notes(notes)
            print("Заметка удалена.")
        else:
            print("Заметка с указанным ID не найдена.")

    def list_notes(self):
        notes = self.note_repository.load_notes()
        for note in notes:
            self.display_note(note)
            print()

    def filter_notes_by_date(self, start_date, end_date):
        notes = self.note_repository.load_notes()
        filtered_notes = [
            note for note in notes
            if start_date <= note.timestamp.split()[0] <= end_date
        ]
        for note in filtered_notes:
            self.display_note(note)
            print()

    @staticmethod
    def display_note(note):
        print(f'ID: {note.id}')
        print(f'Заголовок: {note.title}')
        print(f'Текст: {note.body}')
        print(f'Дата/Время: {note.timestamp}')