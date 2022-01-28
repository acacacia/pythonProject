import this

sudoku1 = [
    [' ', '4', '1', ' ', '5', '2', ' ', '8', ' '],
    [' ', ' ', '7', '3', ' ', ' ', ' ', ' ', '6'],
    ['3', '8', ' ', ' ', '6', '4', ' ', '2', ' '],
    [' ', ' ', ' ', ' ', '2', '9', '4', ' ', '8'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['9', ' ', '2', '1', '4', ' ', ' ', ' ', ' '],
    [' ', '3', ' ', '8', '1', ' ', ' ', '7', '9'],
    ['8', ' ', ' ', ' ', ' ', '5', '3', ' ', ' '],
    [' ', '7', ' ', '2', '9', ' ', '8', '5', ' ']
]

sudoku2 = [
    [' ', ' ', ' ', '7', ' ', ' ', '3', ' ', ' '],
    [' ', '3', ' ', '2', '4', ' ', '1', ' ', ' '],
    ['8', ' ', '6', ' ', '3', ' ', ' ', ' ', '2'],
    [' ', ' ', '9', '1', ' ', ' ', ' ', '2', ' '],
    ['1', '4', ' ', ' ', '9', ' ', ' ', '5', '6'],
    [' ', '5', ' ', ' ', ' ', '6', '9', ' ', ' '],
    ['3', ' ', ' ', ' ', '2', ' ', '6', ' ', '1'],
    [' ', ' ', '4', ' ', '1', '7', ' ', '3', ' '],
    [' ', ' ', '2', ' ', ' ', '4', ' ', ' ', ' ']
]


# 格式化打印
def show(su):
    l = [i for i in range(9)]
    print('', end='    ')
    for i in l:
        print(i, end='    ')
    print()
    index = 0
    for i in su:
        print(index, i)
        index += 1


# 行转列
def category(su):
    f = [i for i in range(9)]
    index = 0
    x = 0
    while x < len(f):
        temp = [i for i in range(9)]
        while index < len(temp):
            temp[index] = su[index][x]
            index += 1
        index = 0
        f[x] = temp
        x += 1
    return f


# 九宫格
def category2(su):
    res = [i for i in range(9)]
    index = 0
    c = 0
    flag = 0
    x = 0
    n = 0
    a = 0
    while a < 3:
        while c < 3:
            temp = []
            while x < 3:
                temp += su[x + n][index:index + 3]
                x += 1
            res[flag] = temp
            flag += 1
            x = 0
            index += 3
            c += 1
        x = 0
        c = 0
        index = 0
        n += 3
        a += 1
    return res


def isNotNull(arr):
    i = 0
    res = []
    while i < len(arr):
        if arr[i] != ' ':
            res += arr[i]
        i += 1
    return res


def position(x, y):
    if x < 3:
        if y < 3:
            return 0
        if 2 < y < 6:
            return 1
        if 4 < y < 9:
            return 2
    if 2 < x < 6:
        if y < 3:
            return 3
        if 2 < y < 6:
            return 4
        if 4 < y < 9:
            return 5
    if 4 < x < 9:
        if y < 3:
            return 6
        if 2 < y < 6:
            return 7
        if 4 < y < 9:
            return 8


def numForNull(arr):
    le = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == ' ':
                le += 1
    return le


sudoku = sudoku2


def primary(su):
    value = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    convert = category(su)
    grid = category2(su)
    count = 0
    sulen = numForNull(su)
    while True:
        if count == sulen:
            break
        for i in range(len(su)):
            for j in range(len(convert)):
                if su[i][j] == ' ':
                    res = value - (set(isNotNull(su[i]) + isNotNull(convert[j]) + isNotNull(grid[position(i, j)])))
                    if len(res) == 1:
                        su[i][j] = list(res)[0]
                        convert = category(su)
                        grid = category2(su)
                        count += 1
    return su


def intermediate(su):
    value = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
    convert = category(su)
    grid = category2(su)
    count = 0
    sulen = numForNull(su)
    dic = {}
    key = []
    for i in range(len(su)):
        for j in range(len(convert)):
            if su[i][j] == ' ':
                res = value - (set(isNotNull(su[i]) + isNotNull(convert[j]) + isNotNull(grid[position(i, j)])))
                if len(res) == 1:
                    su[i][j] = list(res)[0]
                    convert = category(su)
                    grid = category2(su)
                    count += 1
                else:
                    dic[(i, j)] = res
                    key += (i, j),

    index = 2
    keyN = []
    while True:
        if len(keyN) == len(key):
            break
        for i in key:
            if len(dic[i]) == index:
                keyN += i,
        index += 1
    'su[keyN[0][0]][keyN[0][1]] = dic[keyN[0]]'

    for i in keyN:
        for j in dic[i]:
            su[i[0]][i[1]] = j
            show(su)
            intermediate(su)


intermediate(sudoku)


