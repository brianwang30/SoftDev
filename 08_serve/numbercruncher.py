'''
Brian Wang, Jeffery Tang
SoftDev
K06 -- Thinking about jobs
2022-09-29
time spent: 1.5 hr
 DISCO:
  - csv file manipulation in Python (please no)
  - pseudorandom
  - Testing pseudorandom, a lot
  - updating dictionaries
  - dictionary names in python are ALIASES
QCC:
  - how to effectively work with csvs, and other csv readers
 How the script works:
  1. Populate:
      a. We use the csv module to get a csv reader object for occupations.csv
      b. We iterate through each row, storing the name as keys and percents as values in a dictionary
      c. We get rid of the first entry, as it does not contain meaningful info
  2. Rewrite:
      a. We establish a running sum for the percents
      b. We iterate through the dictionary, replacing their percent value with a cumulative percent value
  3. Choose:
      a. We copy the dictionary to save the "total" percent
      b. We get a random number between 0 and total percent
      c. We iterate through the dictionary until we find the job (key) with a percent (value) higher than our randomly selected one
      d. Return the job
 '''

import csv
import random
    
#Randomly choose a student name out of all periods
def choose(dic):
    dic_tmp = dic.copy()
    total = dic_tmp.pop("Total")/2
    rand = random.random() * total
    for job in dic_tmp:
        if rand < dic_tmp.get(job):
            return job
    


#Method to rewrite percentages as cumulative instead of independant
def redef_percent(dic):
    run_sum = 0.0
    for job in dic:
        run_sum = float(dic.get(job)) + run_sum
        dic.update({job:run_sum})
        

def populate(dic):
    #shamelessly stolen from geeksforgeeks (as help!)
    with open("occupations.csv", "r") as f:
        file = csv.reader(f)
                   
        #iterate through all the blocks of info
        for row in file:
            dic[row[0]] = row[1]
    dic.pop("Job Class")
    
    
dictionary = {}
populate(dictionary)
#print(dictionary)
redef_percent(dictionary)
print(choose(dictionary))

#test to test weighted random
test = dictionary.copy()
#wipe the values so we can use as a counter
for job in test:
    test.update({job:0})
#run 100,000 times
for i in range(100000):
    rand = choose(dictionary)
    test.update({rand:test.get(rand) + 1})
#convert big number to small number
for job in test:
    test.update({job:test.get(job)/1000})
#print(test)