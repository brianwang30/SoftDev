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
        choice = random.choice(dictionary[key])
        return "name: " + choice[0] + "\npd: " + key + "\nducky: " + choice[1]
    return "empty"

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
    f = open("krewes.txt", "r")
    file = f.read()
    dic_keys = [] #list of keys because we had some trouble with it
               
    #iterate through all the blocks of info
    while file.find("@@@") > -1:
        #break up the blocks of info
        devo_info = file[0 : file.find("@@@")]
        file = file[file.find("@@@") + 3 :]
        devo_pd = devo_info[0 : devo_info.find("$$$")]
        devo_info = devo_info[devo_info.find("$$$") + 3 :]
        devo_name = devo_info[0 : devo_info.find("$$$")]
        devo_info = devo_info[devo_info.find("$$$") + 3 :]
        devo_ducky = devo_info
        
        #add the new entry
        if devo_pd in dic_keys:
            dic[devo_pd].append([devo_name, devo_ducky])
        else:
            dic[devo_pd] = [[devo_name, devo_ducky]]
            dic_keys.append(devo_pd)
            
dictionary = {}
populate(dictionary)
#print(dictionary)
print(choose(dictionary))
    