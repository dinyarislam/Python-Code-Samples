#!/usr/bin/env python3
"""
Georgia Institute of Technology - CS1301
HW10 - Object Oriented Programming
"""

class Room: # entire class provided
    def __init__(self, name): 
        self.name = name

    def __eq__(self, other):
        return self.name == other.name
        
    def __repr__(self): 
        return "Room(name: {})".format(self.name)

class Task:
    def __init__(self, name):
        self.name = name
        self.isCompleted = False

    def __eq__(self, other):
        return self.name == other.name and self.isCompleted == other.isCompleted 

    def __repr__(self): # provided
        return "Task(name: {}, isCompleted: {})".format(self.name, self.isCompleted)

class Crewmate:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = True
        self.tasksDone = 0

    def doTask(self, task):
        if task.isCompleted == False:
            task.isCompleted = True
            self.tasksDone += 1
        else:
            return "Nothing to do here."

    def vote(self, amus):
        newlist = amus.crewmates + amus.impostors
        for player in newlist:
            if player.name[0] == self.name[0] and player.name != self.name and player.isAlive == True:
                return player
            
    def callMeeting(self, amus):
        newlist = amus.crewmates + amus.impostors
        maxvote = -1
        votedout = ""
        susdict = {}
        for player in newlist:
            susp = player.vote(amus)
            if susp.name in susdict.keys():
                susdict[susp.name] += 1
            else:
                susdict[susp.name] = 1
        for key in susdict.keys():
            if susdict[key] > maxvote:
                votedout = key
                maxvote = susdict[key]
        for crewmate in amus.crewmates:
            if votedout == crewmate.name:
                crewmate.isAlive = False
                return "{} was not An Impostor.".format(votedout)
        for impostor in amus.impostors:
            if votedout == impostor.name:
                impostor.isAlive = False
                return "{} was An Impostor.".format(votedout)
        
 
    def __repr__(self): # provided 
        return "Crewmate(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other): # provided
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class Impostor:
    def __init__(self, name, color, accessories = ()):
        self.name = name
        self.color = color
        self.accessories = accessories
        self.isAlive = True
        self.eliminateCount = 0

    def eliminate(self, player):
        if type(player) != type(self):
            player.isAlive = False
            self.eliminateCount += 1
        else:
            return "They're on your team -_-"
        
    def vote(self, amus):
        newlist = amus.crewmates + amus.impostors
        for player in newlist:
            if player.name[0] == self.name[0] and player.name != self.name and player.isAlive == True:
                return player
            
    def __str__(self):
        return "My name is {} and I'm an impostor.".format(self.name)

    def __repr__(self): # provided
        return "Impostor(name: {}, color: {})".format(self.name, self.color)

    def __eq__(self, other): # provided 
        return (self.name, self.color, self.accessories) == (other.name, other.color, other.accessories)

class AmongUs:
    def __init__(self, maxPlayers):
        self.maxPlayers = maxPlayers
        self.rooms = {}
        self.crewmates = []
        self.impostors = []

    def registerPlayer(self, player):
        if len(self.crewmates + self.impostors) == self.maxPlayers:
            return "Lobby is full."
        else:
            for crewmate in self.crewmates:
                if crewmate.name == player.name:
                    return "Player with name: {} exists.".format(player.name)
            for impostor in self.impostors:
                if impostor.name == player.name:
                    return "Player with name: {} exists.".format(player.name)
            try:
                if player.tasksDone >= 0:
                    self.crewmates.append(player)
            except:
                self.impostors.append(player)

    def registerTask(self, task, room):
        if self.rooms == {}:
            self.rooms[room.name] = [task]
        else:
            for key in self.rooms.keys():
                if task in self.rooms[key] and key != room.name:
                    return "This task has already been registered."
                else:
                    if key == room.name:
                        self.rooms[room.name].append(task)
                    else:
                        self.rooms[room.name] = [task]
                        
                    
    def gameOver(self):
        crewcount = 0
        impostcount = 0
        for crewmate in self.crewmates:
            if crewmate.isAlive == True:
                crewcount += 1
        for impostor in self.impostors:
            if impostor.isAlive == True:
                impostcount += 1
        if crewcount == 0:
            return "Defeat! All crewmates have been eliminated."
        elif impostcount == 0:
            return "Victory! All impostors have been eliminated."
        else:
            return "Game is not over yet!"
        
    def __repr__(self): # provided
        return "AmongUs(maxPlayers: {})".format(self.maxPlayers)

