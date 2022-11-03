#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K19: Give me all your login info pwease
#2022-11-03
#time spent:  hours

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def disp_login():
    print("\n")
    print(request.form['username'])
    return render_template('login.html')



@app.route("/response", methods=['POST'])
def authenticate():
    return render_template('response.html', user=request.form['username'], method=request.method)  #response to a form submission
    
if __name__ == "__main__":
    app.debug = True
    app.run()