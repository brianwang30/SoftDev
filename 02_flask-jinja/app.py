# BWANG (April Li, Brian Wang, Shreya Roy)
# SoftDev
# K10 -- Just Plug It In/Using Templates for our flask apps
# 2022 - 10 - 13
# time spent: 
'''
Disco:

QCC:
Predictions: 
0. The flask app will not be able to use the template, or will just crash 
1. http://127.0.0.1:5000/my_foist_template
2. render_template( TEMPLATE_FILE, TITLE, COLLECTION_TO_BE_LISTED_VERTICALLY )

Results:
0. It cwashed.
1. http://127.0.0.1:5000/my_foist_template
2. render_template( TEMPLATE_FILE, TITLE, COLLECTION_TO_BE_LISTED_VERTICALLY )
just that cool
'''
from flask import Flask, render_template #Q0: What will happen if you remove render_template from this line? (log your prediction before you pull the trigger...)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8,13,"sroy30","is bald"]

@app.route("/my_foist_template") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="not foo", collection=coll) #Q2: What is the significance of each argument? Simplest, most concise answer best.

@app.route("/ambigious") #Q1: Can all of your teammates confidently predict the URL to use to load this page?
def test_tmplt2():
    return render_template( 'its_your_bday.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
