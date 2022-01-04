

"""
Georgia Institute of Technology - CS1301
HW03 - Iteration
"""

#########################################

"""
Function Name: movieNight()
Parameters: a caption (str)
Returns: the fixed caption (str)
"""
def movieNight(caption):
    fixedcaption = ""
    for ch in caption:
        if ch.isdigit() == False:
            fixedcaption += ch
    return fixedcaption

#########################################

"""
Function Name: iceCream()
Parameters: flavor (str), number of vowels (int)
Returns: a sentence (str)
"""
def iceCream(flavor,vowelnum):
    flavorlow = flavor.lower()
    vowelcount = 0
    for ch in flavorlow:
        if ch in "aeiou":
            vowelcount += 1
    if vowelcount > vowelnum:
        return "Yes, {} ice cream has more than {} vowels!".format(flavorlow,vowelnum)
    else:
        return "No, {} ice cream doesn't have more than {} vowels!".format(flavorlow,vowelnum)
    

#########################################

"""
Function Name: dreamCar()
Parameters: car price (float), bank balance(float), interest rate (float)
Returns: number of years (int)
"""
def dreamCar(carprice,balance,intrate):
    if balance >= carprice:
        yearnum = 0
        return yearnum
    yearnum = 1
    newbalance = balance * ((1 + intrate/100) ** yearnum)
    while newbalance < carprice:
        yearnum += 1
        newbalance = balance * ((1 + intrate/100) ** yearnum)
    return yearnum
    

#########################################

"""
Function Name: battleship()
Parameters: board size (int)
Returns: None (NoneType)
"""
def battleship(boardsize):
    letters = "abcdefghijklmnopqrstuvwxyz"
    reqletters = letters[:boardsize]
    for l in reqletters:
        for i in range(1,boardsize):
            print(l + str(i) + " ",end = "")
        print(l + str(boardsize))
    return None
    

#########################################

"""
Function: tennisMatch()
Parameters: player 1 (str), player 2 (str), match record (str)
Returns: winner (str)
"""
def tennisMatch(player1,player2,matchrecord):
    pl1score = 0
    pl2score = 0
    pl1game = 0
    pl2game = 0
    for ch in matchrecord:
        if ch == '-':
            if pl1score > pl2score:
                pl1game += 1
            elif pl2score > pl1score:
                pl2game += 1
            pl1score = 0
            pl2score = 0
            continue
        if ch == '1':
            pl1score += 1
        elif ch == '2':
            pl2score += 1
    if pl1game > pl2game:
        winnerstr = "{} won! The score was {}-{}.".format(player1, pl1game, pl2game)
        return winnerstr
    elif pl2game > pl1game:
        winnerstr = "{} won! The score was {}-{}.".format(player2, pl2game, pl1game)
        return winnerstr
    else:
        return "It's a tie!"


    
    
