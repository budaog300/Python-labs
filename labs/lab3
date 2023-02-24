import os
import json
import csv


directory = "E:\!!!\Pythonlabs\data.csv"
data = {}


# Подсчет количества файлов в папке
def count(path):
    files = [file for file in os.listdir(path) if os.path.isfile(f'{path}/{file}')]
    print(len(files))


# считывание данных из файла в словарь
def parse_csv(directory):
    with open(directory) as file:
        lines = file.read().splitlines()        
        for line in lines:
            (idx, fio, fiov, reason, time) = line.split('\t')
            data.update({int(idx): {"ФИО":fio, "ФИО врача": fiov, "причина обращения": reason, "длительность": int(time)}})
    return data


# запись в файл и добавление нового элемента
def print_data(f, dict, fio, fiov, reason, time):
    for k, v in list(dict.items()):
        f.write(f"№{k}; ФИО: {v['ФИО']}; ФИО врача: {v['ФИО врача']}; причина обращения: {v['причина обращения']}; длительность: {v['длительность']}\n")
    f.write(f"№{len(dict) + 1}; ФИО: {fio}; ФИО врача: {fiov}; причина обращения: {reason}; длительность: {time}\n")
    dict.update({len(dict) + 1: {'ФИО': fio, 'ФИО врача': fiov, 'причина обращения': reason, 'длительность': time}})


# сортировка по строковому полю
def sorted_by_str(data) -> dict:
    return dict(sorted(data.items(), key=lambda x: x[1]["ФИО"], reverse=False))


# сортировка по числовому полю
def sorted_by_number(data) -> dict:
    return dict(sorted(data.items(), key=lambda x: x[1]["длительность"], reverse=False))


# сортировка по критерию
def sorted_dif(data, value) -> dict:
    return dict((k,v) for k,v in data.items() if v["причина обращения"] == value)


# функция записи в файл конечного варианта
def write_to_file():   
    map = parse_csv(directory)  
    with open("E:\!!!\Pythonlabs\yet.csv", "w") as f:
        print_data(f, map, 'Барыбин Андрей Андреевич', 'Ефремов Константин Сергеевич', 'Аппендицит', 2)   


if __name__ == '__main__':
    path = "E:\!!!\Pythonlabs\Лабораторные работы"
    count(path)
    print('Словарь "История посещений поликлиники":')
    for k, v in parse_csv(directory).items():
        print(k,v)
    print('\n')
    print('Сортировка по строковому полю:')
    for k, v in sorted_by_str(parse_csv(directory)).items():
         print(k,v)
    print('\n')
    print('Сортировка по числовому полю:')
    for k, v in sorted_by_number(parse_csv(directory)).items():
        print(k,v)
    print('\n')
    for k, v in sorted_dif(parse_csv(directory), 'ОРВИ').items():
        print('Сортировка по критерию:')
        print(k, v)    
    print('\n')
    print('Функция записи в файл')
    write_to_file()

