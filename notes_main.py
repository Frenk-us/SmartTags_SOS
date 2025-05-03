# Импортируем необходимые инструменты из библиотеки PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,      # Приложение, которое мы будем создавать
    QWidget,           # Окно приложения
    QPushButton,       # Кнопка, на которую можно нажимать
    QLabel,            # Текстовая метка
    QListWidget,       # Список, где будут отображаться элементы
    QLineEdit,         # Поле для ввода текста
    QTextEdit,         # Большое поле для ввода текста
    QInputDialog,      # Окно для ввода данных
    QHBoxLayout,       # Горизонтальная раскладка элементов
    QVBoxLayout,       # Вертикальная раскладка элементов
)
import json  # Модуль для работы с данными в формате JSON
app = QApplication([])
# notes = {
#     "Моя первая заметка": {
#         "текст": "Это самое лучшее приложение для заметок в мире!",
#         "теги": ["добро", "инструкция"],
#     }
# }

# with open("notes_data.json", "w", encoding="utf-8") as file:
#     json.dump(notes, file, sort_keys=True)


# Создаем главное окно приложения
notes_win = QWidget()
notes_win.setWindowTitle("Умные заметки")  # Устанавливаем название окна
notes_win.resize(900, 600)                 # Задаем размер окна (ширина 900, высота 600)
# Создаем виджеты (элементы интерфейса) внутри окна
list_notes = QListWidget()                  # Список заметок
list_notes_label = QLabel("Список заметок") # Метка для списка заметок

# Создаем кнопки для работы с заметками
button_note_create = QPushButton(
    "Создать заметку"
)  # Кнопка для создания новой заметки, при нажатии появится окно для ввода названия
button_note_del = QPushButton("Удалить заметку")   # Кнопка для удаления выбранной заметки
button_note_save = QPushButton("Сохранить заметку") # Кнопка для сохранения текущей заметки
# Создаем элементы для работы с тегами
field_tag = QLineEdit("")                          # Поле для ввода тега
field_tag.setPlaceholderText("Введите тег...")      # Подсказка внутри поля ввода
field_text = QTextEdit()                           # Большое поле для ввода текста заметки
button_tag_add = QPushButton("Добавить к заметке") # Кнопка для добавления тега к заметке
button_tag_del = QPushButton("Открепить от заметки")# Кнопка для удаления тега из заметки
button_tag_search = QPushButton("Искать заметки по тегу") # Кнопка для поиска заметок по тегу
list_tags = QListWidget()                           # Список тегов
list_tags_label = QLabel("Список тегов")            # Метка для списка тегов
# Располагаем виджеты на экране с помощью раскладок (лэйаутов)

# Создаем горизонтальную раскладку для всего окна
layout_notes = QHBoxLayout()

# Создаем первый столбец (вертикальную раскладку) для текста заметки
col_1 = QVBoxLayout()
col_1.addWidget(field_text)  # Добавляем большое поле для текста заметки в первый столбец

# Создаем второй столбец (вертикальную раскладку) для списка заметок и кнопок
col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)  # Добавляем метку "Список заметок"
col_2.addWidget(list_notes)         # Добавляем сам список заметок
# Создаем строку для кнопок создания и удаления заметки
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)  # Добавляем кнопку "Создать заметку"
row_1.addWidget(button_note_del)     # Добавляем кнопку "Удалить заметку"

# Создаем еще одну строку для кнопки сохранения заметки
row_2 = QHBoxLayout()
row_2.addWidget(button_note_save)    # Добавляем кнопку "Сохранить заметку"

# Добавляем строки с кнопками в второй столбец
col_2.addLayout(row_1)
col_2.addLayout(row_2)

# Добавляем метку и список тегов во второй столбец
col_2.addWidget(list_tags_label)      # Метка "Список тегов"
col_2.addWidget(list_tags)             # Сам список тегов

# Добавляем поле для ввода тега во второй столбец
col_2.addWidget(field_tag)             # Поле "Введите тег..."

# Создаем строку для кнопок добавления и удаления тега
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)       # Кнопка "Добавить к заметке"
row_3.addWidget(button_tag_del)       # Кнопка "Открепить от заметки"
# Создаем строку для кнопки поиска по тегу
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)    # Кнопка "Искать заметки по тегу"

# Добавляем строки с кнопками тегов во второй столбец
col_2.addLayout(row_3)
col_2.addLayout(row_4)

# Добавляем оба столбца в основную горизонтальную раскладку
layout_notes.addLayout(col_1, stretch=2)  # Первый столбец занимает больше места
layout_notes.addLayout(col_2, stretch=1)  # Второй столбец занимает меньше места

# Устанавливаем раскладку для главного окна
notes_win.setLayout(layout_notes)

"""Функционал приложения"""

"""Работа с текстом заметки"""

# Функция для добавления новой заметки
def add_note():
    # Открываем диалоговое окно, чтобы пользователь ввел название заметки
    note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки: ")
    if ok and note_name != "":  # Если пользователь нажал ОК и ввел название
        notes[note_name] = {"текст": "", "теги": []}  # Создаем новую заметку с пустым текстом и без тегов
        list_notes.addItem(note_name)                  # Добавляем название заметки в список заметок
        list_tags.addItems(notes[note_name]["теги"])   # Добавляем теги заметки в список тегов (пока пусто)
        # print(notes)  # Можно раскомментировать для отладки

# Функция для отображения выбранной заметки
def show_note():
    # Получаем название заметки, которую выбрал пользователь в списке
    key = list_notes.selectedItems()[0].text()
    # print(key)  # Выводим название заметки в консоль (для проверки)
    field_text.setText(notes[key]["текст"])  # Показываем текст заметки в большом поле
    list_tags.clear()                         # Очищаем список тегов
    list_tags.addItems(notes[key]["теги"])    # Добавляем теги выбранной заметки в список тегов

# Функция для сохранения текущей заметки
def save_note():
    if list_notes.selectedItems():  # Проверяем, выбрана ли какая-то заметка
        key = list_notes.selectedItems()[0].text()        # Получаем название выбранной заметки
        notes[key]["текст"] = field_text.toPlainText()     # Сохраняем текст из большого поля в заметку
        with open("notes_data.json", "w") as file:        # Открываем файл для записи данных
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)  # Сохраняем данные в формате JSON
        print(notes)  # Выводим все заметки в консоль (для проверки)
    else:
        print("Заметка для сохранения не выбрана!")  # Сообщение, если никакая заметка не выбрана

# Функция для удаления выбранной заметки
def del_note():
    if list_notes.selectedItems():  # Проверяем, выбрана ли какая-то заметка
        key = list_notes.selectedItems()[0].text()  # Получаем название выбранной заметки
        del notes[key]                              # Удаляем заметку из словаря
        list_notes.clear()                          # Очищаем список заметок на экране
        list_tags.clear()                           # Очищаем список тегов
        field_text.clear()                          # Очищаем большое поле с текстом заметки
        list_notes.addItems(notes)                  # Добавляем оставшиеся заметки обратно в список
        with open("notes_data.json", "w") as file:  # Открываем файл для записи
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)  # Сохраняем обновленные данные
        print(notes)  # Выводим все заметки в консоль (для проверки)
    else:
        print("Заметка для удаления не выбрана!")

"""Работа с тегами заметки"""

# Функция для добавления тега к заметке
def add_tag():
    if list_notes.selectedItems():  # Проверяем, выбрана ли какая-то заметка
        key = list_notes.selectedItems()[0].text()  # Получаем название выбранной заметки
        tag = field_tag.text()                       # Получаем текст тега из поля ввода
        if not tag in notes[key]["теги"]:            # Проверяем, нет ли уже такого тега у заметки
            notes[key]["теги"].append(tag)           # Добавляем тег к списку тегов заметки
            list_tags.addItem(tag)                    # Показываем тег в списке тегов на экране
            field_tag.clear()                         # Очищаем поле ввода тега
        with open("notes_data.json", "w") as file:    # Открываем файл для записи
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)  # Сохраняем обновленные данные
        print(notes)  # Выводим все заметки в консоль (для проверки)
    else:
        print("Заметка для добавления тега не выбрана!")

# Функция для удаления тега из заметки
# def del_tag():
#     if list_tags.selectedItems():  # Проверяем, выбран ли какой-то тег
#         key = list_notes.selectedItems()[0].text()        # Получаем название выбранной заметки
#         tag = list_tags.selectedItems()[0].text()        # Получаем выбранный тег
#         notes[key]["теги"].remove(tag)                    # Удаляем тег из списка тегов заметки
#         list_tags.clear()                                 # Очищаем список тегов на экране
#         list_tags.addItems(notes[key]["теги"])            # Добавляем оставшиеся теги обратно в список
#         with open("notes_data.json", "w") as file:        # Открываем файл для записи
#             json.dump(notes, file, sort_keys=True, ensure_ascii=False)  # Сохраняем обновленные данные
#     else:
#         print("Тег для удаления не выбран!")  # Сообщение, если никакой тег не выбран

# Функция для удаления тега из заметки
def del_tag():
    if list_tags.selectedItems():  # Проверяем, выбран ли какой-то тег
        key = list_notes.selectedItems()[0].text()        # Получаем название выбранной заметки
        tag = list_tags.selectedItems()[0].text()        # Получаем выбранный тег
        notes[key]["теги"].remove(tag)                    # Удаляем тег из списка тегов заметки
        list_tags.clear()                                 # Очищаем список тегов на экране
        list_tags.addItems(notes[key]["теги"])            # Добавляем оставшиеся теги обратно в список
        with open("notes_data.json", "w") as file:        # Открываем файл для записи
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)  # Сохраняем обновленные данные
    else:
        print("Тег для удаления не выбран!")  # Сообщение, если никакой тег не выбран

# Функция для поиска заметок по тегу
def search_tag():
    # print(button_tag_search.text())  # Выводим текст кнопки в консоль (для проверки)
    tag = field_tag.text()           # Получаем тег из поля ввода
    if button_tag_search.text() == "Искать заметки по тегу" and tag:  # Если кнопка в режиме поиска и тег введен
        # print(tag)  # Выводим тег в консоль (для проверки)
        notes_filtered = {}  # Создаем пустой словарь для найденных заметок
        for note in notes:   # Проходимся по всем заметкам
            if tag in notes[note]["теги"]:  # Если у заметки есть нужный тег
                notes_filtered[note] = notes[note]  # Добавляем заметку в словарь найденных
        button_tag_search.setText("Сбросить поиск")  # Меняем текст кнопки на "Сбросить поиск"
        list_notes.clear()   # Очищаем список заметок на экране
        list_tags.clear()    # Очищаем список тегов
        list_notes.addItems(notes_filtered)  # Добавляем найденные заметки в список
        # print(button_tag_search.text())  # Выводим новый текст кнопки в консоль
    elif button_tag_search.text() == "Сбросить поиск":  # Если кнопка в режиме сброса поиска
        field_tag.clear()                             # Очищаем поле ввода тега
        list_notes.clear()                             # Очищаем список заметок
        list_tags.clear()                              # Очищаем список тегов
        list_notes.addItems(notes)                     # Добавляем все заметки обратно в список
        button_tag_search.setText("Искать заметки по тегу")  # Меняем текст кнопки обратно на "Искать заметки по тегу"
        # print(button_tag_search.text())  # Выводим новый текст кнопки в консоль
    else:
        pass  # Если ни одно условие не выполнено, ничего не делаем

"""Запуск приложения"""

# Подключаем функции к событиям (кнопки будут выполнять наши функции при нажатии)
button_note_create.clicked.connect(add_note)        # При нажатии на "Создать заметку" вызываем функцию add_note
list_notes.itemClicked.connect(show_note)           # При выборе заметки в списке вызываем функцию show_note
button_note_save.clicked.connect(save_note)          # При нажатии на "Сохранить заметку" вызываем функцию save_note
button_note_del.clicked.connect(del_note)            # При нажатии на "Удалить заметку" вызываем функцию del_note
button_tag_add.clicked.connect(add_tag)              # При нажатии на "Добавить к заметке" вызываем функцию add_tag
button_tag_del.clicked.connect(del_tag)              # При нажатии на "Открепить от заметки" вызываем функцию del_tag
button_tag_search.clicked.connect(search_tag)        # При нажатии на "Искать заметки по тегу" вызываем функцию search_tag

# Показываем главное окно приложения на экране
notes_win.show()

# Загружаем сохраненные заметки из файла при запуске приложения
with open("notes_data.json", "r") as file:
    notes = json.load(file)  # Читаем данные из файла и сохраняем их в переменную notes
list_notes.addItems(notes)   # Добавляем все загруженные заметки в список на экране

# Запускаем цикл обработки событий приложения (чтобы окно оставалось открытым и реагировало на действия пользователя)
app.exec_()
