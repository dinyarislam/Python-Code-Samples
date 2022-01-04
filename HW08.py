#!/usr/bin/env python3

import requests

"""
Georgia Institute of Technology - CS1301
HW08 - APIs
"""

"""
Function Name: meetNewPeople()
Parameters: house (str)
Returns: list of people (list)
"""

def meetNewPeople(housename):
    url = "https://www.potterapi.com/v1/characters/?key=$2a$10$kKid7XgqXf36Xq5NoocKMeY4YG25TBIpwO3D7dvHNxphvKOOCwPMa"
    r = requests.get(url)
    datalist = r.json()
    friendlist = []
    for datadict in datalist:
        try:
            if datadict["bloodStatus"] == "pure-blood" and datadict["deathEater"] == False and datadict["house"] == housename:
                friendlist.append(datadict["name"])
        except:
            continue
    return friendlist


"""
Function Name: matchingStudents()
Parameters: character name (str)
Returns: list of students (list)
"""

def matchingStudents(chname):
    studlist = []
    bloodstat = ""
    ahouse = ""
    url = "https://www.potterapi.com/v1/characters/?key=$2a$10$kKid7XgqXf36Xq5NoocKMeY4YG25TBIpwO3D7dvHNxphvKOOCwPMa"
    r = requests.get(url)
    datalist = r.json()
    for datadict in datalist:
        try:
            if datadict["name"] == chname:
                bloodstat = datadict["bloodStatus"]
                ahouse = datadict["house"]
        except:
            continue
    for datadict in datalist:
        try:
            if datadict["bloodStatus"] == bloodstat and datadict["house"] == ahouse and datadict["name"] != chname and datadict["role"] == "student":
                studlist.append(datadict["name"])
        except:
            continue
    return studlist
            

"""
Function Name: similarCharacters()
Parameters: movieID1 (str), movieID2 (str)
Returns: number of people (int)
"""

def similarCharacters(movid1,movid2):
    simchar = 0
    movlist = []
    mov1ch = []
    mov2ch = []
    mov1url = "https://swapi.dev/api/films/" + movid1
    mov2url = "https://swapi.dev/api/films/" + movid2
    m1 = requests.get(mov1url)
    m2 = requests.get(mov2url)
    mov1dict = m1.json()
    mov2dict = m2.json()
    try:
        mov1ch = mov1dict["characters"]
        mov2ch = mov2dict["characters"]
    except:
        return 0
    for mov1 in mov1ch:
        if mov1 in mov2ch and mov1 != movlist:
            movlist.append(mov1)
            simchar += 1
    return simchar


"""
Function Name: spaceDrifting()
Parameters: passengers(int), max price(int)
Returns: list of valid starships (list)
"""

def spaceDrifting(passnum,maxp):
    tuplist = []
    url = "https://swapi.dev/api/starships/?page=1"
    r = requests.get(url)
    stardata = r.json()
    starlist = stardata["results"]
    for shipdict in starlist:
        try:
            if int(shipdict["passengers"]) >= passnum and int(shipdict["cost_in_credits"]) < maxp:
                tuplist.append((shipdict["name"],shipdict["manufacturer"]))
        except:
            continue
    return tuplist
                

"""
Function Name: perfectMatch()
Parameters: list of candidates (list)
Returns: list of potential matches (list)
"""

def perfectMatch(candlist):
    matchlist = []
    url = "https://swapi.dev/api/people/?page=1"
    c = requests.get(url)
    chardata = c.json()
    charlist = chardata["results"]
    for chardict in charlist:
        try:
            if chardict["name"] in candlist and chardict["name"] != "Luke Skywalker" and chardict["name"] != "Darth Vader":
                if int(chardict["height"]) >= 180 and chardict["gender"] == "male":
                    matchlist.append(chardict["name"])
        except:
            continue
    return matchlist

    
