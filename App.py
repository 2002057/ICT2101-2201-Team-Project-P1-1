from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from os import listdir
from os.path import isfile, join, splitext
import json
import hashlib

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

#Route to home page
@app.route('/')
def Index():
    session["name"] = "none"
    return render_template("home.html")

#Route to mapcreation.html
@app.route('/mapcreation')
def mapCreation():
    if session["name"]=="admin":
        return render_template('mapprototype.html')
    else:
        return redirect('/adminlogin')
        
#Route to adminlogin.html
@app.route('/adminlogin')
def adminLogin():
    return render_template('adminlogin.html')

# adminAuth()
# Authenticates admin through community password
# Redirect back to adminlogin if failed
# Redirect to admin page if success
@app.route('/adminauth', methods=['POST'])
def adminAuth():
    password = request.form['password'].replace('\"','')
    pwhash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    with open('static\\pwhash') as f:
        lines = f.readlines()
    result = bool(pwhash == lines[0])
    if result:
        session["name"] = "admin"
        return json.dumps({'success':True, 'text':result}), 200, {'ContentType':'application/json'} 
    else:
        session["name"] = "none"
        return json.dumps({'success':False, 'text':lines[0], 'pwhash':pwhash, 'password':password}), 200, {'ContentType':'application/json'}
        
# saveChallenge()
# Saves challenge map as txt file on local server
@app.route('/receivedata', methods=['POST'])
def saveChallenge():
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

# selectChallenge()
@app.route('/config')
def selectChallenge():

    files = [splitext(f)[0] for f in listdir("challenges\\") if isfile(join("challenges\\", f))]
    return render_template('config.html', files=files)
    

if __name__ == "__main__":
    app.run(debug=True)
    
