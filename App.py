from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import json
app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

import hashlib

#pyserial package and other packages to establish connection with the car
from serial.serialutil import STOPBITS_ONE, Timeout
import serial.tools.list_ports
import serial
from serial import Serial
from time import sleep

#function to communicate with the serial port
def connection():
    serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
    return serialInst

#function to send instruction to the robotic car
def sendInstruction(serialInst,data):
    while not serialInst.isOpen():
        serialInst = connection() 
    serialInst.write(data.encode())
    print(data.encode())

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

#Hash and check password
#Redirect back to adminlogin if failed
#Redirect to admin page if success
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
        
#AJAX Request handling for challenge creation saving
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
        
#Route to instructions page
@app.route('/instructions',methods=['POST'])
def InstructionPage():
    if request.method == 'POST':
        img_selected = request.form['selected_level']
        level_selected = None
        if img_selected == "/static/images/easy1.png":
            level_selected = "/preset_maps/easy1.html"
        elif img_selected == "/static/images/easy2.png":
            level_selected = "/preset_maps/easy2.html"
        elif img_selected == "/static/images/easy3.png":
            level_selected = "/preset_maps/easy3.html"
        elif img_selected == "/static/images/medium1.png":
            level_selected = "/preset_maps/medium1.html"
        elif img_selected == "/static/images/medium2.png":
            level_selected = "/preset_maps/medium2.html"
        elif img_selected == "/static/images/medium3.png":
            level_selected = "/preset_maps/medium3.html"
        elif img_selected == "/static/images/hard1.png":
            level_selected = "/preset_maps/hard1.html"
        elif img_selected == "/static/images/hard2.png":
            level_selected = "/preset_maps/hard2.html"
        elif img_selected == "/static/images/hard3.png":
            level_selected = "/preset_maps/hard3.html"
        return render_template("instructions.html",img=img_selected, level = level_selected)

@app.route('/play',methods=['POST'])
def GamePlay():
    if request.method == 'POST':
        level_sel = request.form['selected_level']
        serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
        while not serialInst.isOpen():
            serialInst = connection() 
        data = request.form.getlist("on")
        data = ' '.join([str(data1) for data1 in data])
        print(data)
        if str(data) == "turn on led":
            sendInstruction(serialInst,str(1))
        if str(data) == "turn off led":
            sendInstruction(serialInst,str(0))
        if str(data) == "move forward":
            sendInstruction(serialInst,"w")
        if str(data) == "brake":
            sendInstruction(serialInst,"s")
        if str(data) == "A brake":
            sendInstruction(serialInst,"a")
        if str(data) == "B brake":
            sendInstruction(serialInst,"d")
        if str(data) == "reverse":
            sendInstruction(serialInst,"x")
        return render_template("gamePlay.html",level = level_sel)

if __name__ == "__main__":
    app.run(debug=True)
    
