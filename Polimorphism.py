class Dog:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def legs(self):
        return self.legs

    def info(self):
        print(f'My name is {self.name} and I have got {self.legs} legs')

    def __str__(self):
        return self.name


class Hen:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

    def legs(self):
        return self.legs

    def info(self):
        print(f'My name is {self.name} and I have got {self.legs} legs')

    def __str__(self):
        return self.name


a = Dog("Jack", 4)
b = Hen("Rose", 2)

for animal in (a, b):
    animal.info()
