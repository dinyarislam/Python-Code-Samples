

"""
Georgia Institute of Technology - CS1301
HW01 - Functions and Expressions
"""

#########################################

"""
Function Name: listen()
Parameters: N/A
Returns: None
"""
def listen():
    songnum = int(input("How many snogs did you listen to?"))
    podcastnum = int(input("How many podcasts did you listen to?"))
    listeningtime_hours = (songnum * 3 + podcastnum * 25)//60
    listeningtime_min = (songnum * 3 + podcastnum * 25)%60
    print("By listening to {} songs and {} podcasts, you have spent {} hours and {} minutes on Spotify.".format(songnum,podcastnum,listeningtime_hours,listeningtime_min))
    return None

#########################################

"""
Function Name: dominosTime()
Parameters: N/A
Returns: None
"""
def dominosTime():
    pizzas = int(input("How many pizzas do you want?"))
    pasta = int(input("How many orders of pasta do you want?"))
    chickenwings = int(input("How many orders of chicken wings do you want?"))
    ordertotal = pizzas * 12 + pasta * 6 + chickenwings * 8
    print("By ordering {} pizzas, {} orders of pasta, and {} orders of chicken wings, your order total comes to ${}.".format(pizzas,pasta,chickenwings,ordertotal))
    return None

#########################################

"""
Function Name: tipAndSplit()
Parameters: N/A
Returns: None
"""
def tipAndSplit():
    ordertotal = int(input("What was the order total?"))
    percentagetip = int(input("What percentage would you like to tip?"))
    peoplenum = int(input("How many people are splitting the order?"))
    tip = percentagetip * ordertotal / 100
    payperperson = (tip + ordertotal) / peoplenum
    print("The driver got a tip of ${}. Each person paid ${}.".format(round(tip,2),round(payperperson,2)))
    return None

#########################################

"""
Function Name: youtuber()
Parameters: N/A
Returns: None
"""
def youtuber():
    videocount = int(input("How many videos have you made?"))
    payperview = float(input("How much do you get paid per view?"))
    viewspervid = int(input("How many views do your videos have?"))
    totalearnings = round(videocount * viewspervid * payperview,2)
    print("You have made ${} by making YouTube videos!".format(totalearnings))
    return None

#########################################

"""
Function Name: bathBomb()
Parameters: N/A
Returns: None
"""
def bathBomb():
    pi = 3.14
    radius = float(input("What is the radius of the bath bomb?"))
    volume = round(4/3 * pi * radius**3, 2)
    print("The volume of a bath bomb with radius {} is {}.".format(radius,volume))
    return None















