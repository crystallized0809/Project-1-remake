Project 1 Redo 

Crystal Li - yl4923

Project description: This is a to-do list app. The front-end is created using html, css, and javascript, and the back-end is created using flask. The app is connected to the mysql database using pymysql. The app is then hosted on AWS using NGinx and gunicorn.
public URL = http://ec2-18-216-213-83.us-east-2.compute.amazonaws.com:5000/

Project Mapping:

app.py - back-end of the app, contains html routes, starts and connects to mysql database. 


README.md - this file

project1remake.pem - the pem file that is the key to access the AWS server.


templates/
-index.html - the front-end of the app
        

      
Instruction of how to run the application:
1. access the AWS instance using the pem file. 
2. set up virulenv by using the command line: source project1env/bin/activate
3. run the app.py file under fold project1 
4. open the app using the URL: http://ec2-18-216-213-83.us-east-2.compute.amazonaws.com:5000/
**install packages as needed such as virtualenv, python, pip, flask, etc. **

