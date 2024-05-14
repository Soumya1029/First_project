def row_validity(row):
    if row.isdigit() and 0<=int(row)<=2 :
        invalid=0
    else:
        invalid=1

    while invalid==1:
        row=(input("Invalid entry, please re-enter the row number where you want to mark: "))
        if row.isdigit() and 0<=int(row)<=2 :
            invalid=0
        else:
            invalid=1
    ar=int(row)
    return ar

def col_validity(col):
    if col.isdigit() and 0<=int(col)<=2:
        invalid=0
    else:
        invalid=1

    while invalid ==1:
        col=(input("Invalid entry, please re-enter the column number where you want to mark: "))
        if col.isdigit() and 0<=int(col)<=2:
            invalid=0
        else:
            invalid=1

    ac=int(col)
    return ac

ttt=[['_','_','_'],['_','_','_'],['_','_','_']]
print(ttt[0])
print(ttt[1])
print(ttt[2])
X_count=0

first_player=input("Please enter the first player's name: ")
second_player=input("Please enter the second player's name: ")

win=0
while win!=1:

    # Player One
    print(first_player, end="")
    row=(input(" enter the row number where you want to mark X: "))
    ar=row_validity(row)

    print(first_player, end="")
    col=(input(" now enter the column number: "))
    ac=col_validity(col)

    if (ttt[ar][ac]=='X')or(ttt[ar][ac]=='O'):
        invalid=1
    else:
        invalid=0
    while invalid==1:
        print(ttt[0])
        print(ttt[1])
        print(ttt[2])
        print(first_player, end="")
        ar=int(input(" invalid entry, Please enter the row number where it is empty: "))
        print(first_player, end="")
        ac=int(input(" invalid entry, Please enter the column number where it is empty: "))
        if (ttt[ar][ac]=='X')or(ttt[ar][ac]=='O'):
            invalid=1
        else:
            invalid=0
    ttt[ar][ac]='X'
    print(ttt[0])
    print(ttt[1])
    print(ttt[2])
    X_count=X_count+1

    if (ttt[0][0]=='X' and ttt[1][1]=='X' and ttt[2][2]=='X') or (ttt[0][0]=='X' and ttt[0][1]=='X' and ttt[0][2]=='X') or (ttt[1][0]=='X' and ttt[1][1]=='X' and ttt[1][2]=='X') or (ttt[2][0]=='X' and ttt[2][1]=='X' and ttt[2][2]=='X') or (ttt[0][0]=='X' and ttt[1][0]=='X' and ttt[2][0]=='X') or (ttt[0][1]=='X' and ttt[1][1]=='X' and ttt[2][1]=='X') or (ttt[0][2]=='X' and ttt[1][2]=='X' and ttt[2][2]=='X') or (ttt[0][2]=='X' and ttt[1][1]=='X' and ttt[2][0]=='X'):
        win=1
        print(first_player, "has won")
        break

    # Draw
    # if (ttt[0][0]=='X' or ttt[0][0]=='0') and (ttt[0][1]=='X' or ttt[0][1]=='0') and (ttt[0][2]=='X' or ttt[0][2]=='0') and (ttt[1][0]=='X' or ttt[1][0]=='0') and (ttt[1][1]=='X' or ttt[1][1]=='0') and (ttt[1][2]=='X' or ttt[1][2]=='0') and (ttt[2][0]=='X' or ttt[2][0]=='0') and (ttt[2][1]=='X' or ttt[2][1]=='0') and (ttt[2][2]=='X' or ttt[2][2]=='0'):
    if X_count==5:
        print("Draw match between", first_player, "and", second_player)
        break

    # Player two
    print(second_player, end="")
    row=(input(" enter the row number where you want to mark X: "))
    br=row_validity(row)

    print(second_player, end="")
    col=(input(" now enter the column number: "))
    bc=col_validity(col)
    
    if (ttt[br][bc]=='X')or(ttt[br][bc]=='O'):
        invalid=1
    else:
        invalid=0
    while invalid==1:
        print(ttt[0])
        print(ttt[1])
        print(ttt[2])
        print(second_player, end="")
        br=int(input( " invalid entry, Please enter the row number where it is empty: "))
        print(second_player, end="")
        bc=int(input( " invalid entry, Please enter the column number where it is empty: "))
        if (ttt[br][bc]=='X')or(ttt[br][bc]=='O'):
            invalid=1
        else:
            invalid=0
    ttt[br][bc]='O'
    print(ttt[0])
    print(ttt[1])
    print(ttt[2])

    if (ttt[0][0]=='O' and ttt[1][1]=='O' and ttt[2][2]=='O') or (ttt[0][0]=='O' and ttt[0][1]=='O' and ttt[0][2]=='O') or (ttt[1][0]=='O' and ttt[1][1]=='O' and ttt[1][2]=='O') or (ttt[2][0]=='O' and ttt[2][1]=='O' and ttt[2][2]=='O') or (ttt[0][0]=='O' and ttt[1][0]=='O' and ttt[2][0]=='O') or (ttt[0][1]=='O' and ttt[1][1]=='O' and ttt[2][1]=='O') or (ttt[0][2]=='O' and ttt[1][2]=='O' and ttt[2][2]=='O') or (ttt[0][2]=='O' and ttt[1][1]=='O' and ttt[2][0]=='O'):
        win=1
        print(second_player, "has won")
        break