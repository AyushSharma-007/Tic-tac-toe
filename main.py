# game of tic-tac-toe
def printGrid():
    for i in l:
        print(i)

def initials():
    player1 = input("Enter your side X/O player -1").upper()
    if player1 == 'X': player2 = 'O'
    else             : player2 = 'X'
    print("Hence player-2 got", player2)
    return player1, player2

def posToRowCol(pos):
    row = d[pos][0]
    col = d[pos][1]
    return row, col
    
def chanceP1():
    while True:
        w = int(input("Choose the position for player1: "))
        row, column = posToRowCol(w)
        if l[row][column] not in 'OX':
            l[row][column] = p1
            printGrid()
            return
        else: 
            print('Position already taken.')
            chanceP1()
def chanceP2():
    v = int(input("Choose the position for player2: "))
    row, column = posToRowCol(v)
    if l[row][column] not in 'OX':
        l[row][column] = p2
        printGrid()
        return
    else:
        print('Position already taken')
        chanceP2()
def getPlayer(ini):
    if ini == 'X':
        if p1 == 'X': return 'Player1'
        else        : return 'Player2'
    else:
        if p1 == 'O': return 'Player1'
        else        : return 'Player2'
def winHor():
    if   l[0][0] == 'X' and l[0][1] == 'X' and l[0][2]  == 'X': return 'X'
    elif l[1][0] == 'X' and l[1][1] == 'X' and l[1][2]  == 'X': return 'X'
    elif l[2][1] == 'X' and l[2][0] == 'X' and l[2][2]  == 'X': return 'X'
    elif l[0][1] == 'O' and l[0][0] == 'O' and l[0][2]  == 'O': return 'O'
    elif l[1][1] == 'O' and l[1][0] == 'O' and l[1][2]  == 'O': return 'O'
    elif l[2][1] == 'O' and l[2][0] == 'O' and l[2][2]  == 'O': return 'O'
    else                                                      : return -1

def winVer():   
    if   l[0][1] == 'X' and l[1][1] == 'X' and l[2][1]  == 'X': return 'X'
    elif l[2][0] == 'X' and l[0][0] == 'X' and l[1][0]  == 'X': return 'X'
    elif l[0][2] == 'X' and l[1][2] == 'X' and l[2][2]  == 'X': return 'X'
    elif l[0][1] == 'O' and l[1][1] == 'O' and l[2][1]  == 'O': return 'O'
    elif l[2][0] == 'O' and l[0][0] == 'O' and l[1][0]  == 'O': return 'O'
    elif l[0][2] == 'O' and l[1][2] == 'O' and l[2][2]  == 'O': return 'O'
    else                                                      : return -1

def winDiag():    
    if   l[0][0] == 'X' and l[1][1] == 'X' and l[2][2]  == 'X': return 'X'
    elif l[2][0] == 'X' and l[1][1] == 'X' and l[0][2]  == 'X': return 'X'
    elif l[0][0] == 'O' and l[1][1] == 'O' and l[2][2]  == 'O': return 'O'
    elif l[2][0] == 'O' and l[1][1] == 'O' and l[0][2]  == 'O': return 'O'
    else                                                      : return -1

def winCheck():
    h = winHor()
    if h == -1:
        v = winVer()
        if v == -1:
            di = winDiag()
            if di == -1: 
                return 0
            else: 
                print(getPlayer(di), 'wins')
                return 1
        else: 
            print(getPlayer(v), 'wins')
            return 1
    else: 
        print(getPlayer(h), 'wins')
        return 1
        
l = [['1','2','3'],
     ['4','5','6'],
     ['7','8','9']]
d = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
print()
print("-----------WELCOME TO THE GAME OF TIC-TAC-TOE-----------")
printGrid()
p1, p2 = initials()
count = 0

while True:
    chanceP1()
    count += 1
    if winCheck(): break
    if count == 9:
        print('Tie')
        break
        
    chanceP2()
    count += 1
    if winCheck(): break
    if count == 9:
        print('Tie')
        break
