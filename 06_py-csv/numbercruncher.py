'''
Brian Wang, Jeffery Tang
SoftDev
K06 -- Thinking about jobs
2022-09-29
time spent: 1 hr
 DISCO:
  - 
 QCC:
  - 
 OPS SUMMARY:
  1. 
 '''

import csv
import random
    
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

def populate(dic):
    f = open("occupations.csv", "r")
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
        #if the pd exists
        if devo_pd in dic_keys:
            dic[devo_pd].append([devo_name, devo_ducky])
        #if the pd does not exist
        else:
            dic[devo_pd] = [[devo_name, devo_ducky]]
            dic_keys.append(devo_pd)
            
dictionary = {}
populate(dictionary)
#print(dictionary)
print(choose(dictionary))
    