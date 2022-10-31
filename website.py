from flask import Flask, render_template
from datetime import date

today = date.today()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html', date = today)

@app.route('/medical')
def index1 ():
    return render_template('Medical.html', date = today)



if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0")

