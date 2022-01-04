

"""
Georgia Institute of Technology - CS1301
HW02 - Conditionals
"""

#########################################

"""
Function Name: skillLevel()
Parameters: passRate (int)
Returns: "Beginner" or "Moderate" or "Advanced" (str)
"""
def skillLevel(passRate):
    if passRate <= 25 and passRate >= 0:
        return "Beginner"
    elif passRate > 25 and passRate <= 75:
        return "Moderate"
    elif passRate > 75 and passRate <= 100:
        return "Advanced"

#########################################

"""
Function Name: bookStore()
Parameters: item (str), walletAmount (float), quantity (int)
Returns: moneyLeftOver (float)
"""
def bookStore(item,walletAmount,quantity):
    moneyLeftOver = 0
    if item == "Shirt" and walletAmount >= (15.50 * quantity):
        moneyLeftOver = walletAmount - (15.50 * quantity)
        return round(moneyLeftOver,2)
    elif item == "Lanyard" and walletAmount >= (4.25 * quantity):
        moneyLeftOver = walletAmount - (4.25 * quantity)
        return round(moneyLeftOver,2)
    elif item == "Sweatshirt" and walletAmount >= (25.00 * quantity):
        moneyLeftOver = walletAmount - (25.00 * quantity)
        return round(moneyLeftOver,2)
    elif item == "Mug" and walletAmount >= (10.50 * quantity):
        moneyLeftOver = walletAmount - (10.50 * quantity)
        return round(moneyLeftOver,2)
    else:
        return "Not enough money!"



        

#########################################

"""
Function Name: dinnerPlans()
Parameters: distance (int), hungerLevel (str)
Returns: transportMode (str)
"""
def dinnerPlans(distance,hungerLevel):
    if distance <= 7 and hungerLevel == "Not Hungry":
        transportMode = "Walk"
    elif distance <= 5 and hungerLevel == "Slightly Hungry":
        transportMode = "Walk"
    elif distance <= 3 and hungerLevel == "Hungry":
        transportMode = "Walk"
    elif distance <= 1 and hungerLevel == "Very Hungry":
        transportMode = "Walk"
    elif distance > 7 and hungerLevel == "Not Hungry":
        transportMode = "Uber"
    elif distance > 5 and hungerLevel == "Slightly Hungry":
        transportMode = "Uber"
    elif distance > 3 and hungerLevel == "Hungry":
        transportMode = "Uber"
    elif distance > 1 and hungerLevel == "Very Hungry":
        transportMode = "Uber"
    return transportMode 
    
        
    

#########################################

"""
Function Name: weekendTrip()
Parameters: distance (float), speed (float), freeTime (float)
Returns: transportMode (str)
"""
def weekendTrip(distance,speed,freeTime):
    travelTime = distance / speed
    if travelTime <= (0.2 * freeTime):
        if speed >= 2.5 and speed <= 15:
            transportMode = "walking"
        elif speed > 15 and speed <= 20:
            transportMode = "biking"
        elif speed > 20:
            transportMode = "driving"
        return transportMode
    elif travelTime > (0.2 * freeTime):
        return "Going to this destination would take too much time."
    
    

#########################################

"""
Function Name: textFriends()
Parameters: distance (float), speed (float), freeTime (float), numSnacks (int), numFriends (int)
Returns: textMsg (str)
"""
def textFriends(distance,speed,freeTime,numSnacks,numFriends):
    travelStatus = weekendTrip(distance,speed,freeTime)
    if travelStatus == "walking" or travelStatus == "biking" or travelStatus == "driving":
        snacksPerPerson = numSnacks // numFriends
        snacksLeft = numSnacks % numFriends
        textMsg = "If each of us gets {} snack(s), there will be {} left. I will be {}, who else is doing the same?".format(snacksPerPerson,snacksLeft,travelStatus)
        return textMsg
    elif travelStatus == "Going to this destination would take too much time.":
        return "Going to this destination would take too much time."

    
    
