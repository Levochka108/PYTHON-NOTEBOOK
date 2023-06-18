import os

from Note import Note
from NoteRepository import NoteRepository

def test_note_repository():
    file_path = "notes.json"
    repository = NoteRepository(file_path)

    # Проверяем загрузку пустого списка заметок
    notes = repository.load_notes()
    assert len(notes) == 0

    # Создаем заметки для добавления
    note1 = Note(1, "Заголовок 1", "Текст 1", "2023-06-18 10:00:00")
    note2 = Note(2, "Заголовок 2", "Текст 2", "2023-06-18 11:00:00")
    note3 = Note(3, "Заголовок 3", "Текст 3", "2023-06-18 12:00:00")

    # Добавляем заметки
    repository.save_notes([note1, note2, note3])

    # Проверяем загрузку добавленных заметок
    notes = repository.load_notes()
    assert len(notes) == 3
    assert notes[0].id == 1
    assert notes[0].title == "Заголовок 1"
    assert notes[0].body == "Текст 1"
    assert notes[0].timestamp == "2023-06-18 10:00:00"

    # Редактируем заметку
    edited_note = Note(2, "Новый заголовок", "Новый текст", "2023-06-18 13:00:00")
    repository.save_notes([edited_note])

    # Проверяем, что редактирование прошло успешно
    notes = repository.load_notes()
    assert len(notes) == 3
    assert notes[1].id == 2
    assert notes[1].title == "Новый заголовок"
    assert notes[1].body == "Новый текст"
    assert notes[1].timestamp == "2023-06-18 13:00:00"

    # Удаляем заметку
    repository.save_notes([note3])

    # Проверяем, что заметка была удалена
    notes = repository.load_notes()
    assert len(notes) == 2
    assert notes[1].id == 2
    assert notes[1].title == "Новый заголовок"
    assert notes[1].body == "Новый текст"
    assert notes[1].timestamp == "2023-06-18 13:00:00"

    # Удаляем созданный файл с заметками
    os.remove(file_path)

# Запускаем тест
test_note_repository()