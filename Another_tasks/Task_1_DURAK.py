# Full
# На вход подаётся 2 карты 
# Нужно вывести YES если первая карта бьёт вторую, и NO в противном случае

def is_win():
    m = input()

    carts = input()

    my, opp = carts.split(' ')

    dost = {"6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
    if my[-1] == m:
        if opp[-1] != m:
            return "YES"
        else:
            if dost[my[0]] > dost[opp[0]]:
                return "YES"
            else: 
                return "NO"

    if my[-1] != opp[-1]:
        return "NO"
    else:
        if dost[my[0]] > dost[opp[0]]:
                return "YES"
        else: 
            return "NO" 
        

print(is_win())
