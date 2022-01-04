#!/usr/bin/env python3
from convert import conversion
"""
Georgia Institute of Technology - CS1301
HW05 - Lists, Tuples, and Modules
"""

"""
Function Name: maskOrders()
Parameters: list organizations (list), list of members (list), mask price (int)
Returns: list of tuples (list)
"""

def maskOrders(orglist, memberlist, mprice):
    totalmoneyowed = 0
    tuplist = []
    combinedtup = ()
    for i in range(len(orglist)):
        totalmoneyowed = memberlist[i] * mprice
        combinedtup = (orglist[i],totalmoneyowed)
        tuplist.append(combinedtup)
    return tuplist
    

"""
Function Name: coffeeBreak()
Parameters: list of drinks (list), budget (float)
Returns: name of drink (str)
"""

def coffeeBreak(drinkslist,spendingbudget):
    withinbudget = False
    drinkchoice = ""
    maxcaff = -1
    for drink in drinkslist:
        if spendingbudget >= drink[2]:
            withinbudget = True
            if drink[1] > maxcaff:
                maxcaff = drink[1]
                drinkchoice = drink[0]
    if withinbudget == True:
        return drinkchoice
    else:
        return None


                


"""
Function Name: myBirthday()
Parameters: gifts (list)
Returns: total balance and gifts (tuple)
"""


def myBirthday(giftslist):
    gifttup = ()
    totalcashgifts = 0
    cashgift = 0
    for gift in giftslist:
        if gift[0] == '$':
            cashgift = conversion(str(gift))
            totalcashgifts += cashgift
        else:
            gifttup = gifttup + (gift,)
    gifttup = ('$' + str(format(totalcashgifts,".2f")),) + gifttup 
    return gifttup

"""
Function Name: roadTrip()
Parameters: state (str), list of tuples (list)
Returns: list of cities (list)
"""

def roadTrip(state,citystate):
    citylist = []
    for location in citystate:
        if state == location[1] and (location[0] not in citylist):
            citylist.append(location[0])
    return citylist


"""
Function Name: safeLocation()
Parameters: list of tuples (list)
Returns: safe locations (list)
"""

def safeLocation(placedetails):
    safeplaces = []
    for place in placedetails:
        if place[1] <= 0.5 * place[2] and place[2] != 0:
            safeplaces.append(place[0])
    return safeplaces


"""
Function Name: eventScheduler()
Parameters: list of tuples (list)
Returns: events (list)
"""

import calendar
def eventScheduler(eventdetails):
    weekendevents = []
    for event in eventdetails:
        if calendar.weekday(2020,event[1],event[2]) == 5 or calendar.weekday(2020,event[1],event[2]) == 6:
            weekendevents.append(event[0])
    return weekendevents



