import numpy as np


# создаем матрицу случайных чисел
def create_matrix():
    random_matrix = np.matrix(np.random.randint(-100, 100, size=(rows, cols)))
    return random_matrix


# создаем результирующую матрицу
def create_result(random_matrix):
    # создаем матрицу из нулей, куда копируем random_matrix
    b = np.append(random_matrix, np.zeros([len(random_matrix), 1], dtype=int), axis=1)
    # c1 = np.hstack((random_matrix, np.zeros((random_matrix.shape[0], 1))))
    result = np.r_[b, [np.array([0] * (cols + 1))]]

    for i in range(rows):
        for j in range(cols):
            if random_matrix[i, j] < 0:
                result[i, cols] += 1
                result[rows, j] += 1

    return result


def pr():
    # выводим исходные данные и результат в файл
    random_matrix = create_matrix()
    result_matrix = create_result(random_matrix)
    with open("lab2.txt", "w") as f:
        f.write('Исходные данные' + '\n\r' + str(random_matrix) + '\n\r' + 'Результат обработки' + '\n\r' + str(result_matrix))
    # print(create_matrix())


if __name__ == '__main__':
    rows = int(input('rows='))
    cols = int(input('cols='))
    pr()
