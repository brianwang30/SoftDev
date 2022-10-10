'''
team BWANG: Shreya Roy (bob), April Li (harambe), Brian Wang (dolphin)
Soft Dev
Period 8
K08 -- serve
2022-10-07
Time spent:
DISCO:
- rediscovered hyperlinks and formatting in HTML
- combining our numbercruncher.py output onto flask app
- BWANG
QCC:
- How would you effectively hide code from a viewer
OPS SUMMARY:
- same dictionary stuff from before
- import csv
- refrence a link

'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
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

#Choose the appropriate reference file
def choose_ref():
    refs = []
    with open("reference.csv", "r") as f:
        file = csv.reader(f)

        #iterate through all the blocks of info
        for row in file:
            refs.append(row[0])
    #our references are subpar
    print(refs)
    return random.choice(refs)

#print(choose_ref())
dictionary = {}
populate(dictionary)
#print(dictionary)
redef_percent(dictionary)



#--------------------------

app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    link = choose_ref()
    return '<a href = ' + link + '>' + choose(dictionary) + "</a>" + "<br><br> - brought to you by BWANG <br>and nothing more<br><br><img src=\"https://i.ytimg.com/vi/ACGRshAYMt8/hqdefault.jpg\" alt = \"why bother\">"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
