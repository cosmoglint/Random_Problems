
mat = [
[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0],
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0],
]


#  lst = [ 0, 1, 2]
        # [3, 4, 5]
        # [6, 7, 8]

def check_row(lst, n):
    myset = set()
    newl = []
    for i in lst[n]:
        if i == 0:
            continue
        else:
            newl.append(i)
            myset.add(i)

    if len(myset) == len(newl):
        return("valid")
    else:
        return "invalid"


def check_column(lst, n):
    myset = set()
    newl = []
    for i in lst:
        if i[n]== 0:
            continue
        else:
            newl.append(i)
            myset.add(i)

    if len(myset) == len(newl):
        return("valid")
    else:
        return("invalid")


def check_square(lst, x, y):
    myset = set()
    newl = []
    startx = x * 3
    stary = y * 3
    for i in range(3): # 0 1 2
        for j in range(3):
            val = lst[ startx + i ][ startx + j ]
            if val== 0:
                continue
            else:
                newl.append(i)
                myset.add(i)

    if len(myset) == len(newl):
        return("valid")
    else:
        return("invalid")


def main():
    print(check_row(mat, 0))


main()
