Math Clone
================

Code to demonstrate 

- how to handle security issue in Flask application.
- use javascript testing framework in project.

Setup
--------------

- pip install requirements.txt
- bower install (bower.json)
- npm install (package.json)


Requirements
------------

- Python 2.7 or 
- virtualenv 
- git
- Network connection (only to install the application)

Setup
-----

**Step 1**: Clone the git repository

    $ git clone https://github.com/benjaminhuanghuang/rest_bank_project.git
    $ cd rest_bank_project

**Step 2**: Create a virtual environment.

For Linux, OSX :

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

For Windows users working on the standard command prompt:

    > virtualenv venv
    > venv\scripts\activate
    (venv) > pip install -r requirements.txt

**Step 3**: Install python library required in project directory

For Linux, OSX :
    (venv) $ pip install -r requirements.txt

For Windows users working on the standard command prompt:
    (venv) > pip install -r requirements.txt
    
Check library version installed:
    (venv) $ pip list
    
**Step 4**: Setup Mongo DB
    # Start mongodb with auth
    $ mongod --dbpath "your db path" --logpath "your log path" --auth

    # Create user for database mathclone
    use mathclone   
    db.createUser({user: "admin",pwd:"abc123",roles: [ { role: "dbOwner", db: "mathclone" } ]})
    db.createUser({user: "webuser",pwd:"abc123",roles: [ { role: "readWrite", db: "mathclone" } ]})
    
    # install Flask-PyMongo
    
**Step 5**: Setup Node 
    $ npm init
    
    
**Step 6**: Setup bower
    $ bower init
    change bower's default components folder?
        Create a .bowerrc file in the root and add following content
            {
                "directory" : "public/components"
            }
    
