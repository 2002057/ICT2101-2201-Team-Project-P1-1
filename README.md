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
- Only commits directly to dev allowed, is to miscellaneous files such as README.md, all code changes are to be done in branches.

Update local repo from GitHub remote/online repo
    ```
    pip install -r requirements.txt
    ```

Create feature branch
    ```
    git cheeckout -b feature/myfeature dev
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
