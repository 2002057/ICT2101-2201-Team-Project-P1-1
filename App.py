from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__, template_folder='templates')


@app.route('/')
def Index():
    return render_template("home.html")

@app.route('/addQueue')
def addQueue():
    return render_template('addQueue.html')

if __name__ == "__main__":
    app.run(debug=True)
