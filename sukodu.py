sudoku = [
    [' ', '4', '1', ' ', '5', '2', ' ', '8', ' '],
    [' ', ' ', '7', '3', ' ', ' ', ' ', ' ', '6'],
    ['3', '8', ' ', ' ', '6', '4', ' ', '2', ' '],
    [' ', ' ', ' ', ' ', '2', '9', '4', ' ', '8'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['9', ' ', '2', '1', '4', ' ', ' ', ' ', ' '],
    [' ', '3', ' ', '8', '1', ' ', ' ', '7', '9'],
    [' ', ' ', ' ', ' ', ' ', ' ', '5', '3', ' '],
    [' ', '7', ' ', '2', '9', ' ', '8', '5', ' ']
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


show(sudoku)


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
                temp += su[x+n][index:index + 3]
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




show(category2(sudoku))
