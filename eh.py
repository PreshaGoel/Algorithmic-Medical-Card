from flask import Flask, render_template, request, redirect, url_for
import csv
import matplotlib.pyplot as plt
from datetime import date

current = date.today()
year1 = current.year

year = []
height = []

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login')
def log():
    return render_template('login.html', failed = 0)

@app.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    student = 2

    with open('pass.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            if row[1] == username and row[2] == password:
                if row[3] == "1":
                    student = row[0]
                    print(student)
                    break
                else:
                    student = 1
                    print(student)
                    break

    if student == 2:
        return render_template("login.html", failed = 1)
    elif student == 1:
        return redirect("/doctors", code = 302)
    else:
        return redirect(url_for("index2", name = student))






@app.route('/doctors')
def index1():
    global name1
    name1 = []
    with open('name.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            name1.append(row[0])

    return render_template('doctors.html', data = name1, year = year1)

@app.route('/parents')
def index2():
    name = request.args["name"]
    data = []
    with open ("name.csv","r") as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            if row[0] == name:
                data = row
                break

    gyna = []

    with open("data.csv", 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader :
            if row[0] == name:
                year.append(row[11])
                height.append(row[12])
                if row[13] == "1":
                    gyna.append("Headache")
                else:
                    gyna.append("")
                if row[14] == "1":
                    gyna.append("Tiredness")
                else:
                    gyna.append("")
                if row[15] == "1":
                    gyna.append("Dizzeness")
                else:
                    gyna.append("")
                if row[18] == "1":
                    gyna.append("Acne")
                else:
                    gyna.append("")
                if row[19] == "1":
                    gyna.append("Facial")
                gyna.append(row[16])
                gyna.append(row[17])
                if row[20] == "1":
                    gyna.append(row[20])
                else:
                    gyna.append("")



    plt.plot(year, height, label = "height")
    plt.xlabel("YEAR")
    plt.ylabel("HEIGHT")
    plt.savefig("static/plot.png")

    return render_template('parents.html', data = data, gyna = gyna)

@app.route('/parents', methods=['POST'])
def myForm():
    name = request.form['name']
    age = request.form['age']
    class1 = request.form['class']
    section = request.form['section']
    roll = request.form['roll']
    adm = request.form['adm']
    fname = request.form['fname']
    focc = request.form['focc']
    mname = request.form['mname']
    mocc = request.form['mocc']
    addr = request.form['addr']

    data = ((name, age, class1, section, roll, adm, fname, focc, mname, mocc, addr))

    with open('name.csv', 'a', newline = '') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(data)

    return render_template('parents.html')

@app.route("/students")
def extract_data():
    student = request.args.get('data')
    students = []
    with open("name.csv", 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            if row[0] == student:
                students.append(row)
                break

    with open("data.csv", 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader :
            if row[0] == student:
                year.append(row[11])
                height.append(row[12])

    plt.plot(year, height, label = "height")
    plt.xlabel("YEAR")
    plt.ylabel("HEIGHT")
    plt.savefig("static/plot.png")

    year.clear()
    height.clear()



    return render_template('student.html', data = students)

@app.route('/doctors', methods=['POST'])
def studentData1():
    name = request.form['name']
    headvalue = request.form['headache']
    tiredvalue = request.form['tiredness']
    height = request.form['height']
    dizzi = request.form['dizziness']
    acne = request.form['acne']
    days = request.form['days']
    interval = request.form['interval']
    facial = request.form['facial']
    remark = request.form['remark']

    student =[]

    with open('name.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)

        for row in reader:
            if row[0] == name:
                student.append(row)


    student.append((year,height, headvalue, tiredvalue, dizzi, days, interval, acne, facial, name, remark))

    final = []

    for i in range (0, 11):
        final.append(student[0][i])


    for data in student[1]:
        final.append(data)


    with open("data.csv", 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)

        writer.writerow(final)

    return render_template ('Doctors.html', data = name1, year = year1)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")