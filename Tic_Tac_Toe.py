def sum(a, b, c):
    return (a+b+c)


def printboard(x, y):
    zero = "X" if x[0] else ("O" if y[0] else 0)
    one = "X" if x[1] else ("O" if y[1] else 1)
    two = "X" if x[2] else ("O" if y[2] else 2)
    three = "X" if x[3] else ("O" if y[3] else 3)
    four = "X" if x[4] else ("O" if y[4] else 4)
    five = "X" if x[5] else ("O" if y[5] else 5)
    six = "X" if x[6] else ("O" if y[6] else 6)
    seven = "X" if x[7] else ("O" if y[7] else 7)
    eight = "X" if x[8] else ("O" if y[8] else 8)

    print(f" {zero} | {one} | {two} ")
    print("---|---|---")
    print(f" {three} | {four} | {five} ")
    print("---|---|---")
    print(f" {six} | {seven} | {eight} ")


def checkwin(x, y):
    cw = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in cw:
        if (sum(x[i[0]], x[i[1]], x[i[2]]) == 3):
            printboard(x, y)
            print("1st Player won the match")
            return 1
            break
        if (sum(y[i[0]], y[i[1]], y[i[2]]) == 3):
            printboard(x, y)
            print("2nd player won the match")
            return 0
            break
        # else:
         #   print("draw match")
    return -1


# # single line terniary operator in ==> print(statement) if true else print(something or))
# printboard()
x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
while True:
    printboard(x, y)
    if turn == 1:
        v = int(input("Enter your value: "))
        x[v] = 1
    else:
        print("2nd Player")
        f = int(input("Enter your value: "))
        y[f] = 1
    turn = 1 - turn
    kw = checkwin(x, y)
    if (kw != -1):

        print("Match Over")
        break
    # else:
    #     print("Draw Match")
