import copy


def get_data():
    data = []
    with open("input.txt") as iFile:
        while True:
            line = iFile.readline()
            if not line:
                break
            temp = (line[:len(line)] + line[len(line) + 1:]).split()
            for x in range(len(temp)):
                temp[x] = int(temp[x])
            data.append(temp)
            print(line, end='')
        print()
    return data


def create_adjacency_matrix(idata):
    matrix = [0] * idata[0][0]
    for x in range(idata[0][0]):
        matrix[x] = [0] * idata[0][0]

    for y in range(1, len(idata)):
        matrix[idata[y][0] - 1][idata[y][1] - 1] = 1
        matrix[idata[y][1] - 1][idata[y][0] - 1] = 1
    return matrix


def create_adjacency_matrix_oriented(idata):
    matrix = [0] * idata[0][0]
    for x in range(idata[0][0]):
        matrix[x] = [0] * idata[0][0]

    for y in range(1, len(idata)):
        matrix[idata[y][0] - 1][idata[y][1] - 1] = 1
    return matrix


def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == -1:
                print("%2s" % ('∞'), end=" ")
            else:
                print("%2d" % matrix[i][j], end=" ")
        print()
    print()


def pow_matrix(matrix1, matrix2):
    temp = copy.deepcopy(matrix2)
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            sum_of_matrix = 0
            for z in range(len(matrix1)):
                sum_of_matrix += matrix1[i][z] * matrix2[z][j]
            temp[i][j] = sum_of_matrix
    return temp


def get_move_matrix(matrix1):
    matrix=copy.deepcopy(matrix1)
    gold_image = copy.deepcopy(matrix)
    in_degree = copy.deepcopy(matrix)
    for x in range(1, len(matrix)):
        in_degree = pow_matrix(in_degree, gold_image)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] > 0 or i == j:
                    continue
                if in_degree[i][j] > 0:
                    matrix[i][j] = x + 1

    for j in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[j][m] == 0 and m != j:
                matrix[j][m] = -1
    show_matrix(matrix)
    return matrix


def find_diameter(move_matrixy):
    digits = []
    for i in range(len(move_matrixy)):
        maximum = move_matrixy[i][0]
        for j in range(len(move_matrixy)):
            if maximum < move_matrixy[i][j] and i != j:
                maximum = move_matrixy[i][j]
        digits.append(maximum)
    maximum = digits[0]
    minimum = digits[0]
    for x in range(1, len(digits)):
        if (maximum < digits[x] and maximum != -1) or digits[x] == -1:
            maximum = digits[x]
        elif (minimum > digits[x] > 0 and digits[x] != -1) or (minimum == -1 and digits[x] >= 0):
            minimum = digits[x]
    print("Діаметр графу: ", end="")
    if maximum != -1:
        print("%d" % maximum)
    else:
        print('∞')
    print("Радіус графа: %d" % minimum)
    print("Центри графу:", end=' ')
    for x in range(len(digits)):
        if minimum == digits[x]:
            print(x + 1, end=" ")
    print()
    return maximum


def get_reachability_matrix(move_matrixes):
    rechability_matrix = copy.deepcopy(move_matrixes)
    for i in range(len(move_matrixes)):
        for j in range(len(move_matrixes)):
            if rechability_matrix[i][j] > 0:
                rechability_matrix[i][j] = 1
            elif rechability_matrix[i][j] == -1:
                rechability_matrix[i][j] = 0
            elif i == j:
                rechability_matrix[i][j] = 1
    return rechability_matrix


def find_tiers_of_graph(move_matrixes, diameters):
    if (diameters == -1):
        diameters = len(move_matrix)
    print("Яруси графу: ")
    for x in range(len(move_matrixes)):
        print("Вершина %s" % (x + 1))
        for y in range(1, diameters + 1):
            print("на відстані %s -" % (y), end=" ")
            for j in range(len(move_matrix)):
                if move_matrix[x][j] == y:
                    print(j + 1, end=" ")
            print()


def is_one(matrixes):
    for i in range(len(matrixes)):
        for j in range(len(matrixes)):
            if (matrixes[i][j] == 0):
                return False
    return True


def transpone_matrix(matrixes):
    size = len(matrixes)
    temp = [0] * size
    for x in range(size):
        temp[x] = [0] * size
    for i in range(size):
        for j in range(size):
            temp[i][j] = matrixes[j][i]
    return temp


def matrix_adding(matrix1, matrix2):
    size = len(matrix1)
    temp = [0] * size
    for x in range(size):
        temp[x] = [0] * size
    for i in range(size):
        for j in range(size):
            temp[i][j] = matrix1[i][j] + matrix2[i][j]
            if temp[i][j] > 1:
                temp[i][j] = 1
    return temp


def pow_in_n_matrix(matrixes):
    k = len(matrixes)
    temp = copy.deepcopy(matrixes)
    for z in range(k):
        temp = pow_matrix(temp, matrixes)

    for i in range(k):
        for j in range(k):
            if (temp[i][j] > 0):
                temp[i][j] = 1
    return temp


def is_simple_conection(matrixe_adjancency):
    imatrix = [0] * len(matrixe_adjancency)
    for x in range(len(matrixe_adjancency)):
        imatrix[x] = [0] * len(matrixe_adjancency)

    for i in range(len(matrixe_adjancency)):
        imatrix[i][i] = 1
    imatrix = matrix_adding(imatrix, transpone_matrix(matrixe_adjancency))
    imatrix = matrix_adding(imatrix, matrixe_adjancency)
    imatrix = pow_in_n_matrix(imatrix)
    return is_one(imatrix)


if int(input("Показати частину (1,2): ")) == 1:
    graph = get_data()
    adjacency = create_adjacency_matrix(graph)
    print("Матриця суміжності: ")
    show_matrix(adjacency)
    print("Матриця відстані: ")
    move_matrix = get_move_matrix(adjacency)
    print("Матриця досяжності: ")
    show_matrix(get_reachability_matrix(move_matrix))
    diameter = find_diameter(move_matrix)
    print()
    find_tiers_of_graph(move_matrix, diameter)
else:
    graph = get_data()
    adjacency = create_adjacency_matrix_oriented(graph)
    print("Матриця суміжності: ")
    show_matrix(adjacency)
    print("Матриця відстані: ")
    move_matrix = get_move_matrix(adjacency)
    print("Матриця досяжності: ")
    rechability_matrix = get_reachability_matrix(move_matrix)
    show_matrix(rechability_matrix)
    print("Тип графу:")
    if is_one(rechability_matrix):
        print("Сильно зв'язаний граф!")
    elif is_one(matrix_adding(rechability_matrix, transpone_matrix(rechability_matrix))):
        print("Однобічна зв'язність")
    elif is_simple_conection(adjacency):
        print("Слабка зв'язність")
    else:
        print("Незв'язний")
