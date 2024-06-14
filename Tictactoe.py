# TO CHECK THE VALIDITY OF THE POSITION ENTERED
def pos_validity(pos):
    while not (pos.isdigit() and 1 <= int(pos) <= 9):
        pos = input("Invalid entry, please re-enter the position number where you want to mark: ")
    return int(pos)

# DEFINING ROW AND COLUMN USING THE POSITION
def position(pos):
    ar = (pos - 1) // 3
    ac = (pos - 1) % 3
    return ar, ac

# INFORMATION REGARDING POSITIONS
print("Please note the positions:")
ttt_numbers=[['1','2','3'],['4','5','6'],['7','8','9']]
for each in ttt_numbers:
    print(' '.join(each))

# NAMING THE PLAYERS
first_player=input("Please enter the first player's name: ")
while len(first_player)==0:
    first_player=input("Please enter a valid first player's name: ")

second_player=input("Please enter the second player's name: ")
while len(second_player)==0:
    second_player=input("Please enter a valid second player's name: ")
while first_player==second_player:
    second_player=input("Both players cannot have the same name. Please enter a valid second player's name: ")

# MAIN BOARD
ttt=[['_','_','_'],['_','_','_'],['_','_','_']]
for each in ttt:
    print(' '.join(each))

X_count=0
win=0
while win!=1:

    # PLAYER ONE TURN
    print(first_player, end="")
    pos=input(" enter the position number where you want to mark X: ")
    pos=pos_validity(pos)
    ar, ac = position(pos)

    while ttt[ar][ac] != '_':
        print("Invalid entry, position already taken.")
        print(first_player, end="")
        pos=input(" enter the position number where you want to mark X: ")
        pos = pos_validity(pos)
        ar, ac = position(pos)

    ttt[ar][ac]='X'
    for each in ttt:
        print(' '.join(each))
    X_count=X_count+1
 
    # DEFINING GAME VICTORY FOR PLAYER ONE
    if (ttt[0][0]=='X' and ttt[1][1]=='X' and ttt[2][2]=='X') or (ttt[0][0]=='X' and ttt[0][1]=='X' and ttt[0][2]=='X') or (ttt[1][0]=='X' and ttt[1][1]=='X' and ttt[1][2]=='X') or (ttt[2][0]=='X' and ttt[2][1]=='X' and ttt[2][2]=='X') or (ttt[0][0]=='X' and ttt[1][0]=='X' and ttt[2][0]=='X') or (ttt[0][1]=='X' and ttt[1][1]=='X' and ttt[2][1]=='X') or (ttt[0][2]=='X' and ttt[1][2]=='X' and ttt[2][2]=='X') or (ttt[0][2]=='X' and ttt[1][1]=='X' and ttt[2][0]=='X'):
        win=1
        print("Congratulations", first_player, "has won")
        break

    # DEFINING DRAW BETWEEN BOTH THE PARTIES
    if X_count==5:
        print("Draw match between", first_player, "and", second_player)
        break

    # PLAYER TWO TURN
    print(second_player, end="")
    pos=input(" enter the position number where you want to mark O: ")
    pos=pos_validity(pos)
    br, bc = position(pos)
    
    while ttt[br][bc] != '_':
        print("Invalid entry, position already taken.")
        print(second_player, end="")
        pos=input(" enter the position number where you want to mark O: ")
        pos = pos_validity(pos)
        br, bc = position(pos)

    ttt[br][bc]='O'
    for each in ttt:
        print(' '.join(each))

    # DEFINING GAME VICTORY FOR PLAYER TWO
    if (ttt[0][0]=='O' and ttt[1][1]=='O' and ttt[2][2]=='O') or (ttt[0][0]=='O' and ttt[0][1]=='O' and ttt[0][2]=='O') or (ttt[1][0]=='O' and ttt[1][1]=='O' and ttt[1][2]=='O') or (ttt[2][0]=='O' and ttt[2][1]=='O' and ttt[2][2]=='O') or (ttt[0][0]=='O' and ttt[1][0]=='O' and ttt[2][0]=='O') or (ttt[0][1]=='O' and ttt[1][1]=='O' and ttt[2][1]=='O') or (ttt[0][2]=='O' and ttt[1][2]=='O' and ttt[2][2]=='O') or (ttt[0][2]=='O' and ttt[1][1]=='O' and ttt[2][0]=='O'):
        win=1
        print("Congratulations",second_player, "has won")
        break