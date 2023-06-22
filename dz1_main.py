import json
import sqlite3

# Открываем и читаем файл
with open('okved_2.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

# Подключаемся к базе данных
conn = sqlite3.connect('hw1.db')

# Создаем таблицу, если она не существует
conn.execute('CREATE TABLE IF NOT EXISTS okved (code TEXT, parent_code TEXT, section TEXT, name TEXT, comment TEXT)')

# Записываем данные в таблицу
for item in data:
    code = item['code']
    parent_code = item.get('parent_code', '')
    section = item['section']
    name = item['name']
    comment = item.get('comment', '')
    
    conn.execute(f"INSERT INTO okved (code, parent_code, section, name, comment) VALUES ('{code}', '{parent_code}', '{section}', '{name}', '{comment}')")

# Сохраняем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()