'''
April Li
SoftDev
K04 -- Dictionaries + RNG
2022-09-23
time spent: 1 hr
DISCO:
 - we learned how to reference dictionaries
 - we learned how to import random and use it
 - we learned how to make test cases :D
 - list() to replace a list of keys
QCC:
 - Is there way to create an object in python like in java, where we can create multiple tests objects and test them off of a static test case?
OPS SUMMARY:
 1) Take in a dictionary
 2) Randomly select a key from the dictionary
 3) Randomly select a element from the list assigned to the key
 4) Return the key and the element
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

##TEST CASE
# pd2 = ["john", "bob"]
# pd7 = ["calvin", "samantha"]
# pd8 = ["man", "woman"]

# krewes1 = {2:pd2, 7:pd7, 8:pd8}
krewes = {
    2:["NICHOLAS",  "ANTHONY",  "BRIAN",  "SAMUEL",  "JULIA",  "YUSHA",  "CORINA",  "CRAIG",  "FANG MIN",  "JEFF",  "KONSTANTIN",  "AARON",  "VIVIAN",  "AYMAN",  "TALIA",  "FAIZA",  "ZIYING",  "YUK KWAN",  "DANIEL",  "WEICHEN",  "MAYA",  "ELIZABETH",  "ANDREW",  "VANSH",  "JONATHAN",  "ABID",  "WILLIAM",  "HUI",  "ANSON",  "KEVIN",  "DANIEL",  "IVAN",  "JASMINE",  "JEFFREY", "Ruiwen"],
    7:["DIANA",  "DAVID",  "SAM",  "PRATTAY",  "ANNA",  "JING YI",  "ADEN",  "EMERSON",  "RUSSELL",  "JACOB",  "WILLIAM",  "NADA",  "SAMANTHA",  "IAN",  "MARC",  "ANJINI",  "JEREMY",  "LAUREN",  "KEVIN",  "RAVINDRA",  "SADI",  "EMILY",  "GITAE",  "MAY",  "MAHIR",  "VIVIAN",  "GABRIEL",  "BRIANNA",  "JUN HONG",  "JOSEPH",  "MATTHEW",  "JAMES",  "THOMAS",  "NICOLE",  "Karen"],
    8:["ALEKSANDRA",  "NAKIB",  "AMEER",  "HENRY",  "DONALD",  "YAT LONG",  "SEBASTIAN",  "DAVID",  "YUKI",  "SHAFIUL",  "DANIEL",  "SELENA",  "JOSEPH",  "SHINJI",  "RYAN",  "APRIL",  "ERICA",  "JIAN HONG",  "VERIT",  "JOSHUA",  "WILSON",  "AAHAN",  "GORDON",  "JUSTIN",  "MAYA",  "FAIYAZ",  "SHREYA",  "ERIC",  "JEFFERY",  "BRIAN",  "KEVIN",  "SAMSON",  "BRIAN",  "HARRY",  "Wanying", "Kevin"]
}

#print(choose(krewes1))
print(choose(krewes))
addPd(3, krewes)
print(choose(krewes))
addStu("mathias", 3, krewes)
print(krewes[3])
print(rmStu("APRIL", 8, krewes))
print(rmStu("APRIL", 8, krewes))
print(krewes[8])
