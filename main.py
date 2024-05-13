# game of tic-tak-toe
def initials():
    player1 = input("Enter your side X/O player -1")
    player2 = 0
    if player1 == 'X':
        player2 == 'O'
        print("Hence payer-2 got O")
    else:
        player2 == 'X'
        print("Hence player-2 got X")
    return player1,player2
def change():
       print("Choose the position where you want to change for player -1 ")
       row = int(input("Enter the row")) 
       coloumn = int(input("Enter the coloumn"))
       l[row][coloumn] = 'X'
       print("Choose the position where you want to change for player -2 ")
       row = int(input("Enter the row")) 
       coloumn = int(input("Enter the coloumn"))
       l[row][coloumn] = 'O'
       print(l) 
def win():
    if l[0][1] and l[0][0] and l[0][2]  == 'X':
        print('player with X wins')
    elif  l[1][1] and l[1][0] and l[1][2]  == 'X':
        print('player with X wins')
    elif l[2][1] and l[2][0] and l[2][2]  == 'X':
        print('player with X wins')

l = [[1,2,3],[4,5,6,],[7,8,9,]]
print()
print("-----------WELCOME TO THE GAME OF TIC-TAK-TOE-----------")
for i in l:
    print(i)
initials()
for i in l:
   
    change()
    win()
