class Animals:
    # Один из методов
    def __init__(self, name):
        self.count = 4
        self.name = name  # Атрибут класса

    def eat(self):
        return "I can eat"

    def sleep(self):
        return "I can sleep"

    def info(self):
        return "I have " + str(self.count) + " legs"

    def __str__(self):
        return self.name

    def setMaxLegs(self, kolvo):
        self.count = kolvo


class Dog(Animals):
    def __init__(self):
        super().__init__("Jack")

    def makesound(self):
        return "Woof"


class Cat(Animals):
    def __init__(self):
        super().__init__("Rose")

    def makesound(self):
        return "Meow"


# Объект класса
a = Dog()
b = Cat()

for animal in (a, b):          # Пример полиморфизма
    print(animal.info())       #
    print(animal.makesound())  #

print(a.sleep())       # Пример вызова методов из разных классов,
print(a.makesound())   # которые где прослеживается наследование

print(a.info())   # Пример использования инкапсуляции
a.setMaxLegs(6)
print(a.info())

# print(type(a))

# print(dir(a))
