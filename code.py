print("Welcome to Tic Tac Toe!")
start = input("To start enter go: ")
xo = [' '] * 9


def game():
    print(xo[0], '|', xo[1], '|', xo[2])
    print(xo[3], '|', xo[4], '|', xo[5])
    print(xo[6], '|', xo[7], '|', xo[8])


def win():
    if (xo[0] == xo[1] == xo[2] == 'X') or (xo[0] == xo[1] == xo[2] == 'O'):
        return "win"
    elif (xo[0] == xo[3] == xo[6] == 'X') or (xo[0] == xo[3] == xo[6] == 'O'):
        return "win"
    elif (xo[0] == xo[4] == xo[8] == 'X') or (xo[0] == xo[4] == xo[8] == 'O'):
        return "win"
    elif (xo[1] == xo[4] == xo[7] == 'X') or (xo[1] == xo[4] == xo[7] == 'O'):
        return "win"
    elif (xo[2] == xo[4] == xo[6] == 'X') or (xo[2] == xo[4] == xo[6] == 'O'):
        return "win"
    elif (xo[2] == xo[5] == xo[8] == 'X') or (xo[2] == xo[5] == xo[8] == 'O'):
        return "win"
    elif (xo[3] == xo[4] == xo[5] == 'X') or (xo[3] == xo[4] == xo[5] == 'O'):
        return "win"
    elif (xo[6] == xo[7] == xo[8] == 'X') or (xo[6] == xo[7] == xo[8] == 'O'):
        return "win"


while start == 'go':
    player1 = ' '
    while player1 != 'X' or 'O':
        player1 = input("Player 1: Do you want to be X or O? ").upper()
        if player1 == 'X':
            player2 = 'O'
            break
        elif player1 == 'O':
            player2 = 'X'
            break
        else:
            player1 = input("Invalid input please enter X or O: ").upper()
            if player1 == 'X':
                player2 = 'O'
            elif player1 == 'O':
                player2 = 'X'
            break
    print("player 1 is:", player1)
    print("player 2 is:", player2)
    print("player 1 will go first")
    game()
    print("Choose a position to play from 1 to 9")
    a = int(input("player1: "))
    xo[a-1] = player1
    game()
    b = int(input("player2: "))
    xo[b - 1] = player2
    game()
    c = int(input("player1: "))
    xo[c - 1] = player1
    game()
    d = int(input("player2: "))
    xo[d - 1] = player2
    game()
    e = int(input("player1: "))
    xo[e - 1] = player1
    game()
    win()
    if win() == "win":
        print("You won congratulations!!!")
        break
    f = int(input("player2: "))
    xo[f - 1] = player2
    game()
    win()
    if win() == "win":
        print("You won congratulations!!!")
        break
    g = int(input("player1: "))
    xo[g - 1] = player1
    game()
    win()
    if win() == "win":
        print("You won congratulations!!!")
        break
    h = int(input("player2: "))
    xo[h - 1] = player2
    game()
    win()
    if win() == "win":
        print("You won congratulations!!!")
        break
    i = int(input("player1: "))
    xo[i - 1] = player1
    game()
    win()
    if win() == "win":
        print("You won congratulations!!!")
        start = input("Do you want to play again? if yes enter go: ")
        xo = [' '] * 9
        break
    else:
        print("Hard luck there's no winner")
    start = input("Do you want to play again? if yes enter go: ")
    xo = [' '] * 9
