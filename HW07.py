#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW07 - File I/O & CSV
"""

"""
Function Name: findCuisine()
Parameters: filename (str), cuisine (str)
Returns: list of restaurants (list)
"""

def findCuisine(textfname,foodtype):
    restlist = []
    filelist = []
    foodtype += "\n"
    afile = open(textfname,"r")
    for currentline in afile:
        filelist.append(currentline)
    for i in range(len(filelist)):
        if filelist[i] == foodtype:
            restname = filelist[i-1][:-1]
            restlist.append(restname)
    afile.close()
    return restlist
        

"""
Function Name: restaurantFilter()
Parameters: filename (str)
Returns: dictionary that maps cuisine type (str) to a 
list of restaurants of the same cuisine type (list)
"""

def restaurantFilter(textfname):
    restlist = []
    cuislist = []
    filelist = []
    restdict = {}
    afile = open(textfname,"r")
    for currentline in afile:
        filelist.append(currentline)
    for i in range(1,len(filelist),4):
        cuislist.append(filelist[i])
    for cuisine in cuislist:
        for i in range(len(filelist)):
            if filelist[i] == cuisine:
                restname = filelist[i-1][:-1]
                try:
                    if restname not in restdict[cuisine[:-1]] and restname != "": 
                        restdict[cuisine[:-1]] += [restname]
                except:
                    restdict[cuisine[:-1]] = []
                    if restname != "":
                        restdict[cuisine[:-1]].append(restname)
    afile.close()
    return restdict
     

"""
Function Name: createDirectory()
Parameters: filename (str), output filename (str)
Returns: None (NoneType)
"""

def createDirectory(textfname,outfname):
    restlist = []
    filelist = []
    grouplist = []
    afile = open(textfname,"r")
    for currentline in afile:
        if currentline[-1] == "\n":
            filelist.append(currentline[:-1])
        else:
            filelist.append(currentline)
    for i in range(0,len(filelist),4):
        if filelist[i] not in restlist:
            restlist.append(filelist[i])
    restlist.sort()
    grouplist = ["Fast Food","Sit-down"]
    dirfile = open(outfname,"w")
    dirfile.write("Restaurant Directory\n\n")
    counter = 1
    restcounter = 0
    for group in grouplist:
        dirfile.write(group + "\n")
        n = 1
        for k in range(len(restlist)):
            j = filelist.index(restlist[k])
            if filelist[j + 2] == group:
                restcounter += 1
                filestr = ""
                filestr = str(n) + ". " + restlist[k] + " - " + filelist[j + 1]
                if restcounter < len(restlist) and counter <= 2:
                    dirfile.write(filestr + "\n")
                else:
                    dirfile.write(filestr)
                n += 1
        counter += 1
        if counter <= 2:
            dirfile.write("\n")
    afile.close()
    dirfile.close()
    return None


"""
Function Name: infectedPercentage()
Parameters: country list(list), filename(str)
Returns: country and percentage (tuple)
"""


def infectedPercentage(countrylist,csvfname):
    infolist = []
    percent = 0
    maxper = -1
    maxtup = ()
    cfile = open(csvfname,"r")
    filelist = cfile.readlines()
    for country in filelist:
        infolist = country.split(',')
        if infolist[0] in countrylist:
            if infolist[2][-1] == '\n':
                percent = int(infolist[2][:-1])/int(infolist[1]) * 100
                if percent > maxper:
                    maxtup = (infolist[0],round(percent,2))
                    maxper = percent
            else:
                percent = int(infolist[2])/int(infolist[1]) * 100
                if percent > maxper:
                    maxtup = (infolist[0],round(percent,2))
                    maxper = percent
    cfile.close()
    if countrylist == []:
        return None
    else:
        return maxtup
        
    
"""
Function Name: countryStatus()
Parameters: country list (list), filename(str)
Returns: risk dictionary (dict)
"""

def countryStatus(countrylist,csvfname):
    riskdict = {"Low risk": [],"Medium risk": [],"High risk": []}
    cfile = open(csvfname,"r")
    filelist = cfile.readlines()
    for country in filelist:
        infolist = country.split(',')
        if infolist[0] in countrylist:
            if infolist[2][-1] == '\n':
                percent = int(infolist[2][:-1])/int(infolist[1]) * 100                   
            else:
                percent = int(infolist[2])/int(infolist[1]) * 100
            if percent <= 25:
                key = "Low risk"
            elif percent > 65:
                key = "High risk"
            else:
                key = "Medium risk"
            riskdict[key].append(infolist[0])
    cfile.close()
    return riskdict
            

"""
Function Name: compareRisk()
Parameters: country to compare (str), country list (list), filename(str)
Returns: compared countries (list)
"""

def compareRisk(compc,countrylist,csvfname):
    retlist = []
    countrypop = 0
    countryinf = 0
    maxpop = 0
    mininf = -1
    cfile = open(csvfname,"r")
    filelist = cfile.readlines()
    for country in filelist:
        infolist = country.split(',')
        if infolist[0] == compc:
            maxpop = int(infolist[1])
            if infolist[2][-1] == '\n':
                mininf = int(infolist[2][:-1])
            else:
                mininf = int(infolist[2])
    for country in filelist:
        infolist = country.split(',')
        if infolist[0] in countrylist:
            countrypop = int(infolist[1])
            if infolist[2][-1] == '\n':
                countryinf = int(infolist[2][:-1])
            else:
                countryinf = int(infolist[2])
            if countrypop < maxpop and countryinf > mininf:
                retlist.append(infolist[0])
    cfile.close()
    if retlist == []:
        return "No countries"
    else:
        return retlist




        


    
