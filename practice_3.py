import csv
import json


# Функция для чтения данных из CSV файла
def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    return data


# Функция для записи данных в CSV файл
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(data)


# Функция для чтения данных из JSON файла
def read_json(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# Функция для записи данных в JSON файл
def write_json(file_path, data):
    with open(file_path, mode='w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


# Пример использования:
# Чтение данных из CSV и JSON файлов
csv_data_read = read_csv('example.csv')
json_data = read_json('example.json')

# Запись данных в CSV и JSON файлы

csv_data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]
if csv_data:
    write_csv('output.csv', csv_data, fieldnames=csv_data[0].keys())
else:
    print("CSV data is empty, nothing to write.")
write_json('output.json', json_data)

print("Данные успешно прочитаны и записаны в файлы.")
