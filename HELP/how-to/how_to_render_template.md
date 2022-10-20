# how-to :: Use an HTML Template with Flask
---
## Overview
Using an HTML template will allow us to pass in certain arguments in render_template
instead of having to write it all in the python script used to run the flask.

### Estimated Time Cost: 0.6 hrs
### Prerequisites:

- Basic flask and html knowledge
- Knowledge of importing modules

0. In a python file of your choice, (ex. `app.py`) in order to render the html template,
 you need to import the render_template module from flask
 ```
 from flask import render_template
 ```
1. Create a templates directory in the same directory as the python file
containing the html file of your choice. This will be the template.
2. In order to have the flask print to a webpage,
make sure to route the file using
```
@app.route("/")
```
This will let the python file print to that page.
3. Write a function where you pass in the html file as an argument for the render_template and then return that result
```
def main():
    return render_template("index.html")
```
4. Now you have flask running a webpage, but what if you want the user to submit data to the webpage? Then, you can pass in arguments into the template file using brackets (ex. `enter your username: {{username}}`)
5. Those arguments can be passed as additional arguments in render_template in the python file.
```
def authenticate():
    return render_template("response.html", username=request.form['username'])
```
6. Profit.

### Resources
* [Additional Tutorial with More Examples](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application)
* [Flask Documentation on Templates](https://flask.palletsprojects.com/en/2.2.x/tutorial/templates/)

---

Accurate as of (last update): 2022-10-20

#### Contributors:  
Anson Wong pd2  
Nicholas Tarsis pd2  
