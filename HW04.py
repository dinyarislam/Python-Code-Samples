"""
Georgia Institute of Technology - CS1301
HW04 - Strings, Indexing and Lists
"""

#########################################

"""
Function Name: findMax()
Parameters: a caption list of numbers (list), start index (int), stop index (int)
Returns: highest number (int)
"""
def findMax(numlist,startpt,stoppt):
    highest = numlist[startpt]
    for number in range(startpt,stoppt + 1):
        if numlist[number] > highest:
            highest = numlist[number]
    return highest
        

#########################################

"""
Function Name: fruitPie()
Parameters: list of fruits (list), minimum quantity (int)
Returns: list of fruits (list)
"""
def fruitPie(fruits,minquantity):
    pieFruits = []
    for i in range(1,len(fruits),2):
        if fruits[i] >= minquantity:
            pieFruits.append(fruits[i - 1])
    return pieFruits
    

#########################################

"""
Function Name: replaceWord()
Parameters: initial sentence (str), replacement word (str)
Returns: corrected sentence (str)
"""
def replaceWord(originalsent,repword):
    correctedsent = ""
    sentwords = originalsent.split(" ")
    for i in range(len(sentwords)):
        if len(sentwords[i]) >= 5:
            sentwords[i] = repword
    correctedsent = sentwords[0]
    for j in range(1,len(sentwords)):
        correctedsent = correctedsent + " " + sentwords[j]
    return correctedsent
      

#########################################

"""
Function Name: highestSum()
Parameters: list of strings (strings)
Returns: index of string with the highest sum (int)
"""
def highestSum(strlist):
    summation = [0 for k in range(len(strlist))]
    for i in range(len(strlist)):
        element = strlist[i]
        for ch in element:
            if ch in "1234567890":
                summation[i] = summation[i] + int(ch)
    maxindex = summation.index(max(summation))
    return maxindex
    

#########################################

"""
Function: sublist()
Parameters: alist (list), blist (list)
Returns: True or False (`boolean`)
"""
def sublist(alist,blist):
    sublistflag = False
    sameelement = 0
    j = 0
    if blist == []:
        sublistflag = True
    elif blist == alist:
        sublistflag = True
    else:
        for i in range(len(alist)):
            if blist[j] == alist[i]:
                sameelement += 1
                j += 1
            else:
                j = 0
            if j == len(blist):
                sublistflag = True
                break
    return sublistflag



