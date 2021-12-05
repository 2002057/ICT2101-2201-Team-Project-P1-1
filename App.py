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

#function to send instruction to the robotic
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

@app.route('/play',methods=['GET','POST'])
def GamePlay():
    if request.method == 'POST':
        level_sel = request.form['selected_level']
       
        return render_template("gamePlay.html",level = level_sel)
        # return render_template("gamePlay.html")
    
@app.route('/forward')
def forward():
    forward = request.args.get('forward')
    print(forward)
    serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
    while not serialInst.isOpen():
        serialInst = connection() 
    if forward == "w":
        sendInstruction(serialInst,"w")
    return ('nothing')

@app.route('/left')
def left():
    left = request.args.get('left')
    print(left)
    serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
    while not serialInst.isOpen():
        serialInst = connection() 
    if left == "a":
        sendInstruction(serialInst,"a")
    return ('nothing')

@app.route('/right')
def right():
    right = request.args.get('right')
    print(right)
    serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
    while not serialInst.isOpen():
        serialInst = connection() 
    if right == "d":
        sendInstruction(serialInst,"d")
    return ('nothing')

@app.route('/back')
def back():
    back = request.args.get('back')
    print(back)
    serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
    while not serialInst.isOpen():
        serialInst = connection() 
    if back == "x":
        sendInstruction(serialInst,"x")
    return ('nothing')

@app.route('/stop')
def stop():
    stop = request.args.get('stop')
    print(stop)
    serialInst = serial.Serial("COM4",9600,parity=serial.PARITY_ODD,stopbits = STOPBITS_ONE)
    while not serialInst.isOpen():
        serialInst = connection() 
    if stop == "s":
        sendInstruction(serialInst,"s")
    return ('nothing')


if __name__ == "__main__":
    app.run(debug=True)
    
