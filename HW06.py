#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW06 - Dictionaries and Try/Except
"""

"""
Function Name: vowelCounter()
Parameters: cities (list)
Returns: number of vowels in each city (dict)
"""

def vowelCounter(citylist):
    vowelnumdict = {}
    for city in citylist:
        vowelcounter = 0
        for letter in city:
            if letter.lower() in "aeiou":
                vowelcounter += 1
        vowelnumdict[city] = vowelcounter
    return vowelnumdict

"""
Function Name: maskDetector()
Parameters: message (list)
Returns: tuple with the location of the mask (str) and the number of errors (int)
"""
def maskDetector(hmessage):
    returntup = ()
    locationstr = ""
    errorcounter = 0
    for ch in hmessage:
        try:
            locationstr += ch
        except:
            errorcounter += 1
    returntup = (locationstr,errorcounter)
    return returntup

"""
Function Name: beautifulDay()
Parameters: dictionary of cities mapped to list of tuples (dict), ideal weather (str), ideal temperature (int)
Returns: a list of places (list)
"""

def beautifulDay(cityweatherdict,iWeather,iTemp):
    citylist = []
    for i in cityweatherdict.keys():
        wpattern = cityweatherdict[i]
        for dailypat in wpattern:
            if dailypat[0] == iWeather:
                if iTemp >= dailypat[1] and iTemp <= dailypat[2]:
                    citylist.append(i)
                    break
    citylist.sort()
    return citylist



"""
Function Name: flightFinder()
Parameters: flight prices by month for different cities (dict), city (str)
Returns: the month with the cheapest flight to the customer's desired city (str) or None
"""

def flightFinder(flightprices,descity):
    lowest = 1000000
    month = ""
    noinfo = True
    insidedict = {}
    for city in flightprices.keys():
        insidedict = flightprices[city]
        if city == descity and insidedict != {}:
            noinfo = False
            for k in insidedict.keys():
                price = insidedict[k]
                if price < lowest:
                    month = k
                    lowest = price
    if noinfo == True:
        return "No Flights"
    else:
        return month
    

"""
Function Name: courseRosters()
Parameters: student info as a list of tuples (list)
Returns: a dictionary containing course rosters (dict)
"""

def courseRosters(studentdata):
    coursedict = {}
    courselist = []
    for info in studentdata:
        for course in info[2]:
            if course not in courselist:
                courselist.append(course)
    for course in courselist:
        majordict = {}
        for info in studentdata:
            if course in info[2]:
                try:
                    majordict[info[1]] += [info[0]]
                except:
                    majordict[info[1]] = []
                    majordict[info[1]].append(info[0])
        coursedict[course] = majordict
    return coursedict



























       
    
    
    




