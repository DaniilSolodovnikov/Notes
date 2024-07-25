import os
import re


def build_note(note_text, note_name):
    try:
        with open(f"{note_name}.txt", "w", encoding="utf-8") as file:
            file.write(note_text)
        print(f"Заметка {note_name} создана.")
    except:
        print('Что-то пошло не так, попробуйте снова')


def create_note():
    note_text = input('Введите текст заметки')
    note_name = input('Введите название заметки')
    build_note(note_text, note_name)


def read_note():
    note_name = input('Введите название заметки')
    if os.path.isfile(note_name):
        with open(note_name, "r") as file:
            content = file.read()
    else:
        print("Заметка не найдена.")


def edit_note():
    note_name = input('Введите название заметки')
    if os.path.isfile(note_name):
        with open(note_name, 'r') as file:
            content = file.read()
            print(content)
        new_content = input('Введите новый текст для заметки')
        if new_content:
            with open(new_content, 'w') as file:
                file.write(new_content)
                print('Заметка успешно обновлена!')
        else:
            print('Обновление отменено.')
    else:
        print('Заметка не найдена.')


def delete_note():
    note_name = input('Введите название заметки')
    if os.path.isfile(note_name):
        os.remove(note_name)
        print('Заметка успешно удалена')
    else:
        print('Заметка не найдена.')


def display_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]
        sorted_notes = sorted(notes, key=len, reverse=True)
        print(
            "Это список всех заметок в порядке от самой короткой до самой длинной: \n",
            sorted_notes,
        )
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


def display_sorted_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]
        sorted_list = sorted(notes, key=len)
        print(
            "\nЭто список заметок в порядке от самой длинной до самой короткой: \n",
            sorted_list,
        )
    except:
        print("Что-то пошло не так. Попробуйте еще раз.")


def main():
    while True:
        action = input(
            "Нажмите цифру, чтобы выбрать действие, которое хотите выполнить с заметками: "
            "\n"
            "Введите 1, чтобы создать заметку с определенным названием и текстом."
            "\n"
            "Введите 2, чтобы вывести на экран нужную вам заметку."
            "\n"
            "Введите 3, чтобы отредактировать нужную вам заметку."
            "\n"
            "Введите 4, чтобы удалить заметку."
            "\n"
            "Введите 5, чтобы вывести все заметки в порядке от самой короткой до самой длинной."
            "\n"
            "Введите 6, чтобы вывести все заметки в порядке от самой длинной до самой короткой."
            "\n"
            "Введите n, чтобы выйти из приложения."
            "\n"
            "Что вы хотите сделать?"
        ).lower()
        allowed_symbols = "123456n"
        pattern1 = "[{0}]".format(allowed_symbols)
        if re.search(pattern1, action):
            print("Вы ввели корректный запрос. Действие сейчас выполнится.")
            if action == "1":
                create_note()
            if action == "2":
                read_note()
            if action == "3":
                edit_note()
            if action == "4":
                delete_note()
            if action == "5":
                display_notes()
            if action == "6":
                display_sorted_notes()
            if action == "n":
                break
        else:
            print(
                "Вы ввели некорректный символ. Пожалуйста, введите цифры от 1 до 6 или n."
            )

        print("Чтобы продолжить работать с заметками, нажмите y/n")
        answer = input().lower()
        if answer != "y":
            break


main()
