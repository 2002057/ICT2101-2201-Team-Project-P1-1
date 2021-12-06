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
    git checkout -b feature/myfeature dev
    ```

Push changes to GitHub from local repo copy
    ```
    git push origin feature/myfeature
    ```

When feature is complete, send a pull request to dev and merge accordingly. Please review with peers if possible.



# UAT


| ID   | Test Case Description                                        | Pre-Condition                 | Steps                                                        | Expected Result                                              | Observed Result | Pass/Fail |
| ---- | ------------------------------------------------------------ | ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | --------------- | --------- |
| ST1  | Open App in Player Mode                                      | None                          | 1. Launch app in admin mode<br />2. Observe screen           | See car connection menu                                      |                 |           |
| ST2  | Open App in Admin Mode                                       | None                          | 1. Launch app in admin mode<br />2. Observe screen           | See configuration-challenge select menu                      |                 |           |
| ST3  | Selecting a challenge to build/edit<br />From Configuration to Challenge Building Mode | In Configuration Mode         | 1. Select level to build or select new level<br />2. Observe screen | See challenge building menu                                  |                 |           |
| ST4  | Save challenge building<br />From Challenge Building mode to Configuration Mode | In Challenge Building Mode    | 1. Select Save<br />2. Observe screen                        | See configuration-challenge select menuUpdated challenge is saved locally |                 |           |
| ST5  | Cancel challenge building<br />From Challenge Building mode to Configuration Mode | In Challenge Building Mode    | 1. Select Cancel<br />2. Observe screen                      | See configuration-challenge select menuChallenge changes are not saved |                 |           |
| ST6  | Select challenge to play<br />From Challenge Selection Menu to Play Mode | In Challenge Selection Menu   | 1. Select level<br />2. Press Play<br />3. Observe screen    | See play menu loaded with selected level map                 |                 |           |
| ST7  | Exit playing challenge<br />From Play Mode to Challenge Select Menu | In Play Mode                  | 1. Select back<br />2. Observe screen                        | See play-challenge select menu                               |                 |           |
| ST8  | Challenge complete From Play Mode to Challenge Completed Screen | In Play Mode                  | 1. Select correct sequence of instructions<br />2. Select Submit<br />3. Observe screen | See challenge complete screen                                |                 |           |
| ST9  | From Challenge Completed Screen to Challenge Selection Menu  | In Challenge Completed Screen | 1. Select continue<br />2. Observe screen                    | See play-challenge select menu                               |                 |           |
| ST10 | Challenge reset                                              | In Play Mode                  | 1. Select reset<br />2. Observe screen                       | See play menu reloaded with fresh instance of selected level map |                 |           |



# Whitebox Testing
For whitebox testing, we wrote tests for def adminAuth() and def receivedata(). These two functions are used for authentication and challenge saving respectively. tests can be found in /tests.
While in the /tests directory, run 
    ```
    python -m pytest
    ```
### Statement coverage 

O - Covered
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



