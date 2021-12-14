from logging import info
from os import name
from flask import Flask,request,render_template

app = Flask(__name__)
all_courses = ["Exploring Computer Science", "ScienceLecA", "ScienceLabA", "English I", "Intro to CS", "CSI", "Unix Lab", "Calculus I", "English II", "Principles of Speech", "CSII", "Comp Org I", "Calculus II", "CSIII", "Software Engineering", "Comp Org II", "Discrete Structures", "ScienceLecB(1)", "ScienceLabB(1)", "ScienceLecB(2)", "ScienceLabB(2)", "Theory of Computation", "Operating Systems", "Fundamentals of Alg.", "Data Communications and Network Programming", "Intro to Cybersecurity 1", "Structure of Prog Languages", "Database Systems", "Technical Writing", "Intro to Linear Algebra", "Senior Project I", "Large Scale Prog.", "Applied Data Science", "Senior Project II"]
clicked = []
not_clicked = []
@app.route('/')
def start():
    return render_template("login.html")
database={'saurav':'123','kaniyah':'aac'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 not in database:
        return render_template('login.html', info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)

@app.route('/page2', methods=['POST','GET'])
def results():
    if request.method == 'POST':
        clicked.append(request.form.getlist('course'))
        print(clicked[0])
    for i in all_courses:
        if i not in clicked[0]:
            not_clicked.append(i)
    print(not_clicked)
    return render_template('page2.html', checked = clicked[0], not_checked = not_clicked)

if __name__== '__main__':
    app.run()