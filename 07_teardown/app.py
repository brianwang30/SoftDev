'''
OINK: Brain(dolphin), Jeffery(mathias), April(horanghae), Wanying(pancake)
Soft Dev
K07 -- Intro to Flask
2022-10-03
time spent:
'''

from flask import Flask

app = Flask(__name__)
    # Q0: Where have you seen similar syntax in other langs?
        # I've seen it in Discord for underlining and italcizing words. markdown

@app.route("/")
    # Q1: What points of reference do you have for meaning of '/'?
        # Signals file location

def hello_world():
    print(__name__)
        # Q2: Where will this print to?
            # Terminal
        # Q3: What will it print?
            # "name" all italicized
    return "No hablo queso!"
        # Q4: Will this appear anywhere? How u know?
            # Where the app is directed to because it is returned rather than printed. We also followed the link.

app.run()
# Q5: Where have you seen similar constructs in other languages?
    #Java my love <3


'''
DISCO:
- Flask will link links
- Rout not root

QCC:
0. Where is this hosted
1. Where is name printed????
2. Why is "__name__" in Flask and also printed?? Do these mean anything. Is it connected?
3. Where is it routing to?? Why use the "@" symbol
4. Why does it use Java syntax
5. Why is flask imported with "__name__", what "__name__" even mean???
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 We used our think juices in conjunction with the computer think juices and executed the code snippet.
'''
