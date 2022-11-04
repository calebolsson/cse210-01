#W01 Prove: Developer       Tic-Tac-Toe         Caleb Olsson
template = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
p = ['x', 'o']


def printBoard():
    print(" " + board[6] + " ║ " + board[7] + " ║ " + board[8])
    print("═══╬═══╬═══")
    print(" " + board[3] + " ║ " + board[4] + " ║ " + board[5])
    print("═══╬═══╬═══")
    print(" " + board[0] + " ║ " + board[1] + " ║ " + board[2])


def placeToken(place, player):
    if place < 1 or place > 9:
        return False
    elif board[place-1] != ' ':
        return False
    else:
        board[place-1] = p[player]
        return True


def resetBoard():
    for i in range(len(board)):
        board[i] = ' '


def lineCheck(a, b, c):
    if a == ' ' or b == ' ' or c == ' ':
        return False
    elif a == b == c:
        return True
    else:
        return False


def checkWin():
    if lineCheck(board[0], board[1], board[2]) or lineCheck(board[3], board[4], board[5]) or lineCheck(board[6], board[7], board[8]):
        return True
    elif lineCheck(board[0], board[3], board[6]) or lineCheck(board[1], board[4], board[7]) or lineCheck(board[2], board[5], board[8]):
        return True
    elif lineCheck(board[0], board[4], board[8]) or lineCheck(board[2], board[4], board[6]):
        return True
    else:
        return False


def checkTie():
    for i in range(len(board)):
        if board[i] == ' ':
            return False
    return True

def main():
    command = 'p'
    while (True):
        print("Welcome!")
        print("├ Press 'p' to play traditional mode")
        print("├ Press 'o' to open the game options")
        print("├ Press 'i' to open the instructions")
        print("├ Press 'u' to play ultimate tic-tac-toe")
        command = input()
        if command == '' or command[0] == 'e' or command[0] == 'q':
            break
        elif command == 'u':
            print("Game mode currently unavailable")
        elif command == 'i':
            for i in range(len(board)):
                board[i] = str(i+1)
            print("Tic-Tac-Toe is played according to the following rules.")
            print("1. The game is played on a grid that is three squares by three squares.")
            print("2. Player one uses " + p[0] +
                "'s. Player two uses " + p[1] + "'s.")
            print("3. Players take turns putting their marks in empty squares.")
            print("4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.")
            print("5. If all nine squares are full and neither player has three in a row, the game ends in a draw.")
            input("Press [enter] to continue")
            print("While taking a turn, input the number that corresponds to where you want to play your mark:")
            printBoard()
            input("Press [enter] to continue")
            resetBoard()
        elif command == 'o':
            print("Options:")
            print("├ 1 - Change p1 mark ( "+p[0]+" )")
            print("├ 2 - Change p2 mark ( "+p[1]+" )")
            command = input()
            if command == '1' or command == '2':
                player = int(command) - 1
                other = player + 1
                if player == 1:
                    other == other - 2
                newMark = input(
                    "Select new mark (was "+p[player]+", cannot be "+p[other]+", or empty):")
                if newMark[0] == '' or newMark[0] == p[0] or newMark == p[1]:
                    print("Error: mark not changed")
                else:
                    p[player] = newMark[0]
                    print("Mark set to "+p[player])
        elif command == 'p':
            resetBoard()
            playing = True
            player = 0
            while playing:
                printBoard()
                token = input("Player "+str(player+1)+": ")
                if token == '':
                    print("Please select valid position")
                elif token[0] == 'q' or token[0] == 'e':
                    playing = False
                elif ord(token[0]) > 57 or ord(token[0]) < 49:
                    print("Please select valid position")
                elif placeToken(int(token[0]), player):
                    if checkWin():
                        print("Player "+str(player+1)+" wins!")
                        printBoard()
                        input("Press [enter] to continue")
                        playing = False
                    elif checkTie():
                        print("Tie!")
                        printBoard()
                        input("Press [enter] to continue")
                        playing = False
                    elif player == 0:
                        player += 1
                    else:
                        player -= 1
                elif playing:
                    print("Please select valid position")
    print("END OF LINE")

main()