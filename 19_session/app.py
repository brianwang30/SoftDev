#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K19: Give me all your login info pwease
#2022-11-03
#time spent:  hours

from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key="HI"

@app.route('/', methods=['GET'])
def disp_login():
    
    if 'username' in session:
        return render_template('auth.html', user=session['username'], passw=session['password'], method=request.method)
    return render_template('login.html')
    


@app.route("/auth", methods=['POST'])
def authenticate():
    ex_user = "mykolyk"
    ex_pass = "foofoo"
    #if request.method == 'POST' and request.form['username'] == ex_user and request.form["password"] == ex_user:
    if request.method == 'POST':
        print(request.form)
        if request.form['username'] == ex_user and request.form["password"] == ex_pass:
            session['username']=request.form['username']
            session['password']=request.form['password']
            return render_template('auth.html', user=request.form['username'], passw=request.form['password'], method=request.method)  #response to a form submission

    return render_template('error.html')

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    #wipe login info cookies
    print("hi")
    session.pop('username')
    session.pop('password')
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True
    app.run()