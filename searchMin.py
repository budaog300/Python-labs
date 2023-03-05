from random import randint

list = []


def input_data():
    try:
        n = int(input())
    except ValueError:
        print("Oops! Need integer data type... (n)")
        return
    for i in range(n):
        list.append(randint(0, 10))


def main():
    mini = list[0]
    for i in list:
        if i < mini:
            mini = i
    return mini


def pr():
    print(list)
    print(main())


if __name__ == '__main__':
    input_data()
    pr()
