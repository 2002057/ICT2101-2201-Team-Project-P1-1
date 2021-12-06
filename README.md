# ICT2101-2201-Team-Project-P1-1
Group Members:
1. Chen Xin Xin, Student ID 2002169
2. Yao Yu Jing, Student ID 2001452
3. Lim Jia Jin Randall, Student ID 2002057
4. Vanessa Ho Jing Mei, Student ID 2002030

# Getting Started

1. Clone the repo to anywhere you want.

2. On Visual Studio Code, open up terminal.

3. To install the required packages of the project:
    ```
    pip install -r requirements.txt
    ```
3. To start running the python flask app:
    ```
    python App.py
    ```
4. On the terminal, it should say "Running on [URL]", Ctrl+Click on the URL to open up the application on your browser.

# Notes
- Please do "pip install -r requirements.txt" on your terminal, or else you might have errors when running the application.
- Documentation for the FLASK CRUD APP can be found [here](https://codeloop.org/flask-crud-application-with-sqlalchemy/).

# Development Workflow
- All features will branch from dev, and each team member could work on the feature assign to them. 
- All feature related development is to be done on separate feature branches.
- Only changes to miscellaneous files such as README.md are allowed to commit directly to dev branch, all code changes are to be done in respective feature branches.

Update local repo from GitHub remote/online repo
    ```
    git pull origin
    ```

Create feature branch
    ```
    git checkout -b feature/myfeature dev
    ```

Commit often during development
    ```
    git commit -m "commit message"
    ```

Push changes to GitHub from local repo copy
    ```
    git push origin feature/myfeature
    ```

When feature is complete, send a pull request to dev and merge accordingly. Please review with peers if possible.



# UAT


| ID   | Test Case Description                                        | Pre-Condition                 | Steps                                                        | Expected Result                                              | Observed Result | Pass/Fail |
| ---- | ------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- | --------- |
| ST1  | Open App in Player Mode                                      | None                          | 1. Launch app in player mode<br />2. Observe screen           | See Home page                                      | See as expected result                | Pass          |
| ST2  | Open App in Admin Mode                                       | None                          | 1. Login in admin mode<br />2. Observe screen           | See configuration-challenge select menu                      | See as expected result                | Pass          |
| ST3  | Allow user to build a map challenge/edit<br />From Admin mode build your own map | In Admin Mode         | 1. Design your own map<br />2. Key in name for the map <br />3. Click on 'save' button<br />4. Observe screen | See successful message and the map being save                                  | See successful message but map not being saved                | Fail          |
| ST4  | Select challenge to play<br />From Challenge Selection Menu to Play Mode | In Challenge Selection Menu   | 1. Select level<br />2. Press Play<br />3. Observe screen    | See play page loaded with selected level map                 |  See as expected result               | Pass          |
| ST5  | Challenge complete From Play page | In Play page                  | 1. Select correct sequence of instructions<br />2. Select Submit<br />3. Observe screen | See success messgae and direct to Home page                                | See as expected result                | Pass          | 
| ST6  | Change fail due to out of border  | In Play page | 1. Select steps that caused the car to go out of the border<br />2. Observe screen                    | See out of border message and play page reloaded with fresh instance of selected level map                               | See as expected                | Pass          |
| ST7 | Change fail due to wrong path                                              | In Play page                  | 1. Select steps that caused the car to reach the white panel<br />2. Observe screen                       | See wrong panel message and play page reloaded with fresh instance of selected level map |  See as expected result               | Pass          |



# Whitebox Testing
For whitebox testing, we wrote tests for def adminAuth() and def receivedata(). These two functions are used for authentication and challenge saving respectively. tests can be found in /tests.</br>
In order for test to run, the application iself must also be running as instructed in "Getting Started"</br>
While in the /tests directory, run 
    ```
    python -m pytest tests.py
    ```

![Alt Text](https://i.imgur.com/0yaLyoR.gif)

### Statement coverage 

O - Covered</br>
X - Not Covered

##### def adminAuth(): 1/1

###### test_adminAuth_success(): 8/11

```
def adminAuth():
O    password = request.form['password'].replace('\"','')
O    pwhash = hashlib.sha256(password.encode('utf-8')).hexdigest()
O    with open('static\\pwhash') as f:
O        lines = f.readlines()
O    result = bool(pwhash == lines[0])
O    if result:
O        session["name"] = "admin"
O        return json.dumps({'success':True, 'text':result}), 200, {'ContentType':'application/json'} 
X    else:
X        session["name"] = "none"
X        return json.dumps({'success':False, 'text':lines[0], 'pwhash':pwhash, 'password':password}), 200, {'ContentType':'application/json'}

```

###### test_adminAuth_fail(): 9/11

```
def adminAuth():
O    password = request.form['password'].replace('\"','')
O    pwhash = hashlib.sha256(password.encode('utf-8')).hexdigest()
O    with open('static\\pwhash') as f:
O        lines = f.readlines()
O    result = bool(pwhash == lines[0])
O    if result:
X        session["name"] = "admin"
X        return json.dumps({'success':True, 'text':result}), 200, {'ContentType':'application/json'} 
O    else:
O        session["name"] = "none"
O        return json.dumps({'success':False, 'text':lines[0], 'pwhash':pwhash, 'password':password}), 200, {'ContentType':'application/json'} 

```

##### def receivedata(): 10/12

###### test_adminAuth_success(): 7/12

```
def receivedata():
O    mapStr = request.form['map']
O    fileName = request.form['name'] 
O    map = json.loads(mapStr)
X    if not fileName:
X        print('emptyfilename')
X        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'} 
O    try:
O        with open("challenges\\"+fileName+".txt", "w") as fo:
O            fo.write(mapStr)
O        return json.dumps({'success':True, 'text':'Challenge saved'}), 200, {'ContentType':'application/json'} 
X    except:
X        return json.dumps({'success':False, 'text':'Challenge not saved'}), 200, {'ContentType':'application/json'}     

```

###### test_adminAuth_fail(): 6/12

```
def receivedata():
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

```



