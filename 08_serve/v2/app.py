'''
team BWANG: Shreya Roy, April Lee, Brian Wang
Soft Dev
Period 8
K08 -- serve
2022-10-06
Time spent: .2 hr

Prediction: line 26 will print __main__ after "about to print __name__"
            in the command line. No hablo queso will appear as normal.
Result: Every time the link is refreshed, the method hello_world() is
        ran, and lines 25 and 26 are printed in the terminal, with
        no hablo queso appearing on the site.

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
    return "No hablo queso!"

app.run()

