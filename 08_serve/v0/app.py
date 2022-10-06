'''
team BWANG: Shreya Roy, April Lee, Brian Wang
Soft Dev
Period 8
K08 -- serve
2022-10-06
Time spent: .2 hr

Prediction: this file will print name in terminal
Result: it did not print name in terminal.

'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) # ...

@app.route("/") # ...
def hello_world():
    print(__name__) # ...
    return "No hablo queso!"  # ...

app.run()  # ...
                
