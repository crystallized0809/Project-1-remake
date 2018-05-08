# project1 information

group name in amazon group setting : cs1122
public url :http://18.219.118.210
##Members:

Santiago Rendon: sr4670

Andrey Khegay: ak6585

Dorothy Ng: dn1131

Nahom Molla: nym228

Yujia Zhang: yz4184

Project discription: This is a project using html, css java script as front end, python flask, mysql(pymysql) as backend. The content is a todo list that can get content, modify content and delete content. With the help of ec2 instance setup, connect with nginx and gunicorn, it can be accessed by anyserver using the url http://18.219.118.210

##Project Mapping:

app.py - starts server and contains app routes,connecting with database

frontend.html - contains HTML to-do list(front-end), as well as some backend script

README.md - Project Information


templates/
-index.html - Renders front page for app, includes text and buttons, some css formatting, and script
        
static/
-js/
--backend.py - Finishes Sprint 2, functions and logic behind frontend
        
idea/
-misc.xml - Helps with crossing out to-do list items
-modules.xml - Module manager for crossing out to-do list
-vcs.xml - Contaning mapping for Directory
      
Instruction of how to run the application:
1.if on local server, run the app.py file (the folder tempelate with html file should in same directory as this python file) in debug mode. Go to localhost, which is http://127.0.0.1:5000, to see the application
2. if request remotely, go to http://18.219.118.210
