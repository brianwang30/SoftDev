'''
team BWANG: Shreya Roy, April Li, Brian Wang
Soft Dev
Period 8
K08 -- serve
2022-10-06
Time spent: .2 hr

Prediction: Name of app will not appear in terminal, but no hablo
            queso will still show up.
Result: __main__ is not printed in terminal after the link. No hablo
        queso still appears as normal.

'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

