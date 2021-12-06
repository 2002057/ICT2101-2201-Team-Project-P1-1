from requests import Session
import json
session = Session()

#Statement coverage 
#O - Covered
#X - Not Covered


#def adminAuth():
#O    password = request.form['password'].replace('\"','')
#O    pwhash = hashlib.sha256(password.encode('utf-8')).hexdigest()
#O    with open('static\\pwhash') as f:
#O        lines = f.readlines()
#O    result = bool(pwhash == lines[0])
#O    if result:
#O        session["name"] = "admin"
#O        return json.dumps({'success':True, 'text':result}), 200, {'ContentType':'application/json'} 
#X    else:
#X        session["name"] = "none"
#X        return json.dumps({'success':False, 'text':lines[0], 'pwhash':pwhash, 'password':password}), 200, {'ContentType':'application/json'}
def test_adminAuth_success():
    response = session.post(
        url='http://localhost:5000/adminauth',
        data={
            'password': 'password'
        },
        headers={
            'Referer': 'http://localhost:5000/adminlogin'
        }
    )
    assert response.text == "{\"success\": true, \"text\": true}"
  

#Odef adminAuth():
#O    password = request.form['password'].replace('\"','')
#O    pwhash = hashlib.sha256(password.encode('utf-8')).hexdigest()
#O    with open('static\\pwhash') as f:
#O        lines = f.readlines()
#O    result = bool(pwhash == lines[0])
#O    if result:
#X        session["name"] = "admin"
#X        return json.dumps({'success':True, 'text':result}), 200, {'ContentType':'application/json'} 
#O    else:
#O        session["name"] = "none"
#O        return json.dumps({'success':False, 'text':lines[0], 'pwhash':pwhash, 'password':password}), 200, {'ContentType':'application/json'} 
def test_adminAuth_fail():
    response = session.post(
        url='http://localhost:5000/adminauth',
        data={
            'password': 'wrongpassword'
        },
        headers={
            'Referer': 'http://localhost:5000/adminlogin'
        }
    )
    assert "{\"success\": false," in response.text
    
#Odef receivedata():
#O    mapStr = request.form['map']
#O    fileName = request.form['name'] 
#O    map = json.loads(mapStr)
#X    if not fileName:
#X        print('emptyfilename')
#X        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'} 
#O    try:
#O        with open("challenges\\"+fileName+".txt", "w") as fo:
#O            fo.write(mapStr)
#O        return json.dumps({'success':True, 'text':'Challenge saved'}), 200, {'ContentType':'application/json'} 
#X    except:
#X        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'}     
def test_receivedata_success():
    response = session.post(
        url='http://localhost:5000/receivedata',
        data={
            "map": "{\"1\":\"white\",\"2\":\"white\",\"3\":\"white\",\"4\":\"white\",\"5\":\"white\",\"6\":\"white\",\"7\":\"white\",\"8\":\"white\",\"9\":\"white\",\"10\":\"white\",\"11\":\"white\",\"12\":\"white\",\"13\":\"white\",\"14\":\"white\",\"15\":\"black\",\"16\":\"white\",\"17\":\"white\",\"18\":\"white\",\"19\":\"white\",\"20\":\"white\",\"21\":\"white\",\"22\":\"white\",\"23\":\"white\",\"24\":\"white\",\"25\":\"white\",\"26\":\"white\",\"27\":\"white\",\"28\":\"white\",\"29\":\"white\",\"30\":\"white\",\"31\":\"white\",\"32\":\"white\",\"33\":\"white\",\"34\":\"white\",\"35\":\"white\",\"36\":\"white\"}",
            "name": "test"
        },
        headers={
            'Referer': 'http://localhost:5000/mapcreation'
        }
    )
    assert response.text == "{\"success\": true, \"text\": \"Challenge saved\"}"


#Odef receivedata():
#O    mapStr = request.form['map']
#O    fileName = request.form['name'] 
#O    map = json.loads(mapStr)
#O    if not fileName:
#O        print('emptyfilename')
#O        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'} 
#X    try:
#X        with open("challenges\\"+fileName+".txt", "w") as fo:
#X            fo.write(mapStr)
#X        return json.dumps({'success':True, 'text':'Challenge saved'}), 200, {'ContentType':'application/json'} 
#X    except:
#X        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'}     
def test_receivedata_fail():
    response = session.post(
        url='http://localhost:5000/receivedata',
        data={
            "map": "{\"1\":\"white\",\"2\":\"white\",\"3\":\"white\",\"4\":\"white\",\"5\":\"white\",\"6\":\"white\",\"7\":\"white\",\"8\":\"white\",\"9\":\"white\",\"10\":\"white\",\"11\":\"white\",\"12\":\"white\",\"13\":\"white\",\"14\":\"white\",\"15\":\"black\",\"16\":\"white\",\"17\":\"white\",\"18\":\"white\",\"19\":\"white\",\"20\":\"white\",\"21\":\"white\",\"22\":\"white\",\"23\":\"white\",\"24\":\"white\",\"25\":\"white\",\"26\":\"white\",\"27\":\"white\",\"28\":\"white\",\"29\":\"white\",\"30\":\"white\",\"31\":\"white\",\"32\":\"white\",\"33\":\"white\",\"34\":\"white\",\"35\":\"white\",\"36\":\"white\"}",
            "name": ""
        },
        headers={
            'Referer': 'http://localhost:5000/mapcreation'
        }
    )
    assert response.text == "{\"success\": false, \"text\": \"Challenge not saved\"}"
    
    
    
    
    
    
    