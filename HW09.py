#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW09 - Recursion
"""

"""
Function Name: pickyEater()
Parameters: food list (list)
Returns: number of food items that can be eaten (int)
"""

def pickyEater(flist):
    if len(flist) == 0:
        return 0 
    elif len(flist) != 0:
        if len(flist[0]) % 2 == 0 and flist[0] != "":
            return 1 + pickyEater(flist[1:])
        else:
            return 0 + pickyEater(flist[1:])
    

"""
Function Name: inviteFriends()
Parameters: list of invitees (list)
Returns: flattened list of all invitees (list)
"""

def inviteFriends(ilist):
    if len(ilist) == 0:
        return []
    if type(ilist[0]) == str:
        return [ilist[0]] + inviteFriends(ilist[1:])
    else:
        return inviteFriends(ilist[0]) + inviteFriends(ilist[1:])


"""
Function Name: friendsgiving()
Parameters: stores (list), budget (float), maxDistance (int)
Returns: price of sauce at each store (dict)
"""

def friendsgiving(tuplist,bud,maxd):
    if len(tuplist) == 0:
        return {}
    sdict = friendsgiving(tuplist[1:],bud,maxd)
    if tuplist[0][1] < bud and tuplist[0][2] < maxd:
        sdict[tuplist[0][0]] = tuplist[0][1]
    return sdict


"""
Function Name: palindrome()
Parameters: string (str), guess (int)
Returns: Whether the string contains a number of palindromes (bool)
"""

def palindrome(pstr,guess):
    substr = pstr[:3]
    if len(substr) != 3:
        if guess != 0:
            return False
        else:
            return True
    else:
        if substr[0] == substr[2] and (substr[1] != substr[0] and substr[1] != substr[2]):
            guess -= 1
            return palindrome(pstr[1:],guess) 
        else:
            return palindrome(pstr[1:],guess)
    if guess != 0:
        return False
    else:
        return True

