from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import json
app = Flask(__name__, template_folder='templates')


@app.route('/')
def Index():
    return render_template("home.html")

@app.route('/mapcreation')
def mapCreation():
    return render_template('mapprototype.html')

@app.route('/receivedata', methods=['POST'])
def receivedata():
    mapStr = request.form['map']
    fileName = request.form['name'] 
    map = json.loads(mapStr)
    if not fileName:
        print('emptyfilename')
        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'} 
    try:
        with open("challenges\\"+fileName+".txt", "w") as fo:
            fo.write(mapStr)
        return json.dumps({'success':True, 'text':'Challenge saved'}), 200, {'ContentType':'application/json'} 
    except:
        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'} 
if __name__ == "__main__":
    app.run(debug=True)
