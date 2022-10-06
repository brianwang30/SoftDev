'''
team BWANG: Shreya Roy, April Lee, Brian Wang
Soft Dev
Period 8
K08 -- serve
2022-10-06
Time spent: .2 hr


Prediction: Line 32 will show futher detail and information about app
            in the terminal when the program is first ran.

Result: Terminal says Debug mode: on, and that debugger is active,
        and we are given a pin. The output when refreshed is the
        exact same. When the file is updated, the debugger detects a
        change, and says so in the terminal.

'''
# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!!"

app.debug = True
app.run()
