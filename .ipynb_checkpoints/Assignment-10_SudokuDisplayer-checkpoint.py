sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

countouter = 0
for outer in sudoku:
    if countouter % 3 == 0:
        print(11 * "- ")
    else:
        next
    countinner = 0
    for inner in outer:
        if countinner == 0:
            next
        elif countinner % 3 == 0:
            print("|", end=" ")
        print(inner, end=" ")
        countinner += 1
    print("")
    countouter += 1

print(11 * "- ")