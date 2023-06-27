
from datetime import datetime
import json


notes = []
path = 'work_1/notes.json'


def open_notes():
    global notes
    try:
        with open(path, 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        pass


def save_notes():
    with open(path, 'w') as file:
        json.dump(notes, file)


def menu():
    return '''Главное меню:
    1. Открыть список заметок
    2. Добавить заметки
    3. Изменить заметки
    4. Удалить заметки
    5. Выход'''


def add_note():
    id_note = 1
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    added_at = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    for note in notes:
        if note['id'] == id_note:
            id_note += 1
    note = {'id': id_note, 'title': title, 'body': body,
            'added_at': added_at, 'updated_at': added_at}
    notes.append(note)
    
    notes.sort(key= lambda x: x['id'])

    save_notes()
    print('Заметка сохранена!')

def open_list_notes():
    for note in notes:
        print(f"id: {note['id']}, Заголовок: {note['title']}, Тело заметки: {note['body']}, Создана в: {note['added_at']}, Обновлена в: {note['updated_at']}")
    if not notes:
        print('Нет заметок!')
        
def change_note():
    id_note = int(input('Введите id заметки, которую необходимо изменить: '))
    for note in notes:
        if note['id'] == id_note:
            note['title'] = input('Введите заголовок: ')
            note['body'] = input('Введите текст: ')
            note['updated_at'] = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            save_notes()
            print('Заметка изменена!')
            break
    else:
        print('Заметка не найдена!')

add_note()

while True:
    print(menu())
    choice = int(input('Выберите пункт меню: '))
    match choice:
        case 1:
            open_list_notes()
        case 2:
            add_note()
        case 3:
            change_note()
        case 4:
            pass
        case 5:
            break

