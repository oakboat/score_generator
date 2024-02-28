from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        registration = request.form['registration']
        admission = request.form['admission']
        score1 = request.form['score1']
        score2 = request.form['score2']
        score3 = request.form['score3']
        score4 = request.form['score4']
        total = request.form['total']
        return render_template("index.html", login = True, name = name, registration = registration, admission = admission, score1 = score1, score2 = score2,
        score3 = score3, score4 = score4, total = total)
    else:
        return render_template("index.html", login = False)
    