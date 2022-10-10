'''
team BWANG: Shreya Roy, April Li, Brian Wang
Soft Dev
Period 8
K08 -- serve
2022-10-06
Time spent: .2 hr

Prediction: Only when __name__ is "__main__", the debugger runs like
            v3 of app.py. Otherwise, it will run like v2 of app.py.
Result: Runs identical to v3 of app.py, unless the "__main__" string in
        the conditional is altered in any way, then app does not run at
        all.

'''

# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2022

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
