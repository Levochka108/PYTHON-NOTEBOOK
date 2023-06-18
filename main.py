import datetime
from NoteManager import NoteManager
from NoteRepository import NoteRepository


def main_menu():
    note_repository = NoteRepository("notes.json")
    note_manager = NoteManager(note_repository)

    while True:
        print("=== Меню ===")
        print("1. Вывести все заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Фильтровать заметки по дате")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            note_manager.list_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)
        elif choice == "3":
            note_id = input("Введите ID заметки для редактирования: ")
            new_title = input("Введите новый заголовок (оставьте пустым, чтобы не изменять): ")
            new_body = input("Введите новый текст (оставьте пустым, чтобы не изменять): ")
            note_manager.edit_note(note_id, new_title, new_body)
        elif choice == "4":
            note_id = input("Введите ID заметки для удаления: ")
            note_manager.delete_note(note_id)
        elif choice == "5":
            start_date = input("Введите начальную дату в формате ГГГГ-ММ-ДД: ")
            end_date = input("Введите конечную дату в формате ГГГГ-ММ-ДД: ")
            note_manager.filter_notes_by_date(start_date, end_date)
        elif choice == "0":
            break
        else:
            print("Некорректный выбор.")


if __name__ == "__main__":
    main_menu()
