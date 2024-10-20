import csv


def read_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        result = [row for row in csv_reader]
    return result


def write_csv(file_path, ready_data):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(ready_data)


def process_data(input_data):
    # Операция: умножение чисел на 2
    result_data = []
    for row in input_data:
        result_row = [str(int(value) * 2) for value in row]
        result_data.append(result_row)
    return result_data


if __name__ == "__main__":
    input_file = 'data.csv'
    output_file = 'output.csv'

    # Чтение данных из CSV-файла
    data = read_csv(input_file)

    # Обработка данных
    processed_data = process_data(data)

    # Запись результатов в новый CSV-файл
    write_csv(output_file, processed_data)

    print("Данные успешно обработаны и записаны в файл.")
