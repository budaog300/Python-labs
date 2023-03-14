import os


def count(path):
    files = [file for file in os.listdir(path) if os.path.isfile(f'{path}/{file}')]
    print('Количество файлов в папке = ' + str(len(files)))


class Index:
    def __init__(self, idx: int):
        self.idx = idx

    def get_idx(self):
        return self.idx

    def set_idx(self, val):
        self.idx = val


class Map(Index):
    idx, fio, fiov, reason, time = 0, '', '', '', 0

    def __init__(self, idx: int, fio: str, fiov: str, reason: str, time: int):
        super().__init__(idx)
        self.idx = idx
        self.fio = fio
        self.fiov = fiov
        self.reason = reason
        self.time = time

    def __str__(self):
        return f'№{self.idx}  ФИО: {self.fio}, ФИО врача: {self.fiov}, причина обращения: {self.reason}, длительность: {self.time}'

    def __repr__(self):
        return f'№{self.idx}  ФИО: {self.fio}, ФИО врача: {self.fiov}, причина обращения: {self.reason}, длительность: {self.time}'


class Main:
    data = {}
    path = ''
    path2 = ''
    num = 0

    def __init__(self, f, g):
        self.path = f
        self.data = self.parse_csv(f)
        self.path2 = g

    def __repr__(self):
        return f'Map({[repr(r) for r in self.data]})'

    def __setattr__(self, item, value):
        self.__dict__[item] = value

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым числом")
        if 0 <= item < len(self.data):
            return self.data[item]
        else:
            raise IndexError("Неверный индекс")

    # def __getitem__(self, item):
    #     return self.data[item]

    def generator(self, f):
        self.num = 0
        with open(f):
            while self.num < len(self.data):
                yield self.data[self.num]
                self.num += 1

    # Генератор с условием
    # def gen(self, f, value):
    #     with open(f) as file:
    #         gener = (i for i in file if value in i)
    #         for i in gener:
    #             return i

    @staticmethod
    def parse_csv(f):
        d = []
        with open(f) as file:
            lines = file.read().splitlines()
            for line in lines:
                (idx, fio, fiov, reason, time) = line.replace("\n", "").split(";")
                d.append(Map(int(idx), fio, fiov, reason, int(time)))
        return d

    def print_data(self):
        for r in self.data:
            return f"№{r.idx} ФИО: {r.fio}; ФИО врача: {r.fiov}; причина обращения: {r.reason}; длительность: {r.time}\n"

    def add(self, fio, fiov, reason, time):
        self.data.append(Map(len(self.data) + 1, fio, fiov, reason, time))
        self.write_to_file(self.path2, self.data)

    def sorted_by_str(self):
        return sorted(self.data, key=lambda x: x.fio, reverse=False)

    def sorted_by_number(self):
        return sorted(self.data, key=lambda x: x.time, reverse=False)

    def sorted_dif(self, value):
        list = []
        for r in self.data:
            if r.reason == value:
                list.append(r)
        return list

    @staticmethod
    def write_to_file(output, d):
        with open(output, "w") as f:
            for r in d:
                f.write(
                    f"№{r.idx} ФИО: {r.fio}; ФИО врача: {r.fiov}; причина обращения: {r.reason}; длительность: {r.time}\n")
        with open(output) as f:
            print(f.read())


class Counter(Main):
    data = {}
    num = -1

    def __init__(self, f, g):
        super().__init__(f, g)
        self.data = self.parse_csv(f)

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        while self.num < len(self.data):
            return self.data[self.num]
        raise StopIteration


if __name__ == '__main__':
    path = "E:\!!!\Pythonlabs\Лабораторные работы"
    directory = "data.csv"
    output = "yet.csv"
    count(path)
    print('\n')
    data = Main(directory, output)
    print('Словарь "История посещений поликлиники":')
    for r in data.parse_csv(directory):
        print(r)
    print('\n')

    # __repr__
    print('Пример работы __repr__:')
    print(repr(data), "\n")
    print('\n')

    # __getitme__
    print('Пример работы __getitme__:')
    print(data[1])
    print('\n')

    # Итератор
    print('Итератор:')
    it = Counter(directory, output)
    for item in it:
        print(item)
    # i = iter(data.parse_csv(directory))
    # print(next(i))
    print('\n')

    # Генератор
    print('Генератор:')
    for item in data.generator(directory):
        print(item)
    # print(data.gen(directory, "ОРВИ"))
    print('\n')

    # Добавление нового элемента в словарь
    print('Обновленный словарь:')
    print(data.add('Бабкевич Андрей Андреевич', 'Ефремов Константин Сергеевич', 'Аппендицит', 2))

    print('Сортировка по строковому полю:')
    for r in data.sorted_by_str():
        print(r)
    print('\n')
    print('Сортировка по числовому полю:')
    for r in data.sorted_by_number():
        print(r)
    print('\n')
    print('Сортировка по критерию:')
    for r in data.sorted_dif('Артроз коленного сустава'):
        print(r)
