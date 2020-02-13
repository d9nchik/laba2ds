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


def get_move_matrix(matrix):
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
    show_matrix(matrix)
    for j in range(len(matrix)):
        for m in range(len(matrix[0])):
            if matrix[j][m] == 0 and m != j:
                matrix[j][m] = -1

    return matrix


def find_diameter(move_matrixy):
    digits = []
    for i in range(len(move_matrixy)):
        maximum = move_matrixy[i][0]
        for j in range(len(move_matrixy)):
            if maximum < move_matrixy[i][j]:
                maximum = move_matrixy[i][j]
        digits.append(maximum)
    maximum = digits[0]
    minimum = digits[0]
    for x in range(1, len(digits)):
        if maximum < digits[x]:
            maximum = digits[x]
        elif (minimum > digits[x] > 0) or (minimum < 1 and digits[x] > 0):
            minimum = digits[x]
    print("Діаметр графу: %d" % maximum)
    print("Радіус графа: %d" % minimum)
    print("Вершини графу:", end=' ')
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
    return rechability_matrix


def find_tiers_of_graph(move_matrixes, diameter):
    print("Яруси графу: ")
    for x in range(len(move_matrixes)):
        print("Вершина %s" % (x + 1))
        for y in range(1, diameter + 1):
            print("на відстані %s -" % (y), end=" ")
            for j in range(len(move_matrix)):
                if move_matrix[x][j] == y:
                    print(j + 1, end=" ")
            print()



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
    show_matrix(get_reachability_matrix(move_matrix))
