'''
Brian Wang, Jeffery Tang
SoftDev
K05 -- Further Dictionaries and File Reading
2022-09-28
time spent: 1 hr
DISCO:
 QCC:
 OPS SUMMARY:
 '''

import random as random
    
#Randomly choose a student name out of all periods
def choose(dictionary):
    #Randomly select a key from the available keys in the dictionary
    key = list(dictionary)[random.randint(0,len(list(dictionary))-1)]
    #return(random.choice(dictionary[list(dictionary)[random.randint(0,len(list(dictionary))-1)]]))
    
    #if class is not empty
    if len(dictionary[key]) > 0:
        #Return the randomly selected key along with a randomly selected element in the list associated with the key
        return str(key) + ": " + random.choice(dictionary[key])
    return "class " + str(key) + " is empty"

def addPd(pd, dictionary):
    dictionary[pd] = []

def rmPd(pd, dictionary):
    return dictionary.pop(pd)

def addStu(name, pd, dictionary):
    dictionary[pd].append(name)
    
def rmStu(name, pd, dictionary):
    for e in range(len(dictionary[pd])):
        if dictionary[pd][e] == name:
            return dictionary[pd].pop(e)
    return "no student with " + name + " found"

def populate(dic):
    file = open("krewes.txt", "r")
    while file.find("@@@") > -1:
        devoInfo = file[0, file.find("@@@")]
        file = file[file.find("@@@") + 3 :]
        devoPd = devoInfo[0, devoInfo.find("$$$")]
        devoInfo = devoInfo[devoInfo.find("$$$") + 3 :]
        devoName = devoInfo[0, devoInfo.find("$$$")]
        devoInfo = devoInfo[devoInfo.find("$$$") + 3 :]
        defoDucky = devoInfo
        if dic.index(devoPd) 
dictionary = {}
    