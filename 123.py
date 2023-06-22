import zipfile
import json
import sqlite3

with zipfile.ZipFile('okved_2.json.zip', 'r') as myzip:
    # получаем список имен файлов в архиве
    filenames = myzip.namelist()
    # итерируемся по каждому файлу
    for filename in filenames:
        #print(filename)
        # читаем содержимое файла в формате JSON
        myzip.extract(filename)
        with myzip.open(filename) as myfile:
            data = json.load(myfile)  
            #print(data[:2])          
            # проверяем, содержит ли файл ключ 'okved'
            if 'okved_2' in data:
            # итерируемся по каждому классификатору в файле
                for okved in data['okved']:
                    code = okved['code']
                    parent_code = okved.get('parent_code', None)
                    section = okved.get('section', None)
                    name = okved.get('name', None)
                    comment = okved.get('comment', None)
                    # записываем данные в базу данных
                    conn = sqlite3.connect('hw1.db')
                    c = conn.cursor()
                    c.execute(f"INSERT INTO okved (code, parent_code, section, name, comment) VALUES ('{code}', '{parent_code}', '{section}', '{name}', '{comment}')")
                    conn.commit()
                    conn.close()