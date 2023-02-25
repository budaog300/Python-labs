from random import randrange, randint

a = [3, 2, 7, 5, 2, 1, 2, 6, 3, 9]
b = [1, 2, 5, 4, 8]
c = []
d = []
list = []
list1 = []
flag = False


# result =  2 7 5 2 1 2 6.
def input_data():
    # способ с рандомным вводом данных
    try:
        n = int(input())
    except ValueError:
        print("Oops! Need integer data type... (n)")
        return
    try:
        k = int(input())
    except ValueError:
        print("Oops! Need integer data type... (k)")
        return
    for i in range(n):
        list.append(randint(0, 10))
    for i in range(k):
        list1.append(randint(0, 10))


def append_data():
    flag = False
    for i in list:
        if int(i) % 2 != 0:
            d.append(i)
        else:
            flag = False
            d.clear()

        if len(d) != 0:
            for elementd in d:
                if elementd in list1:
                    flag = True
                    break
            if flag:
                for elementd in d:
                    c.append(elementd)
        else:
            c.append(i)
            flag = False


def pr():
    print(list)
    print(list1)
    print(format(c))


if __name__ == '__main__':
    input_data()
    append_data()
    pr()
