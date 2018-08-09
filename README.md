# Instagramcloned
#### Instagram - Clone
 ## Description
This is an application where a user can sign up login and choose to share images with other users whom the user has followed.
 ## Setup and installations
 #### Prerequisites
1. [Python3.6](https://www.python.org/downloads/)
2. [Postgres](https://www.postgresql.org/download/)
3. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
4. [Pip](https://pip.pypa.io/en/stable/installing/)
 #### Technologies used
    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
 #### Clone the Repo and checkout into the project folder.
```bash
git clone git@github.com:Kaundu/instagramclone.git && cd instagramclone
```
 #### Create and activate the virtual environment
```bash
python3.6 -m virtualenv virtual
```
 ```bash
source virtual/bin/activate
```
 #### Setting up environment variables
Create a `.env` file and paste paste the following filling where appropriate:
```
SECRET_KEY='<Secret_key>'
DBNAME='insta'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True
 ```
 #### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
 #### Create the Database
In a new terminal, open the postgresql shell with `psql`.
```bash
CREATE DATABASE insta;
```
 #### Make and run migrations
```bash
python3.6 manage.py makemigrations && python3.6 manage.py migrate
```
 #### Run the app
```bash
python3.6 manage.py runserver
```
Open [localhost:8000](http://127.0.0.1:8000/)
 ## Deployment
To deploy the application, please follow the instructions in [this gist](https://gist.github.com/newtonkiragu/42f2500e56d9c2375a087233587eddd0)
 ## Contributing
Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)
 ## Bugs
- A user cannot like nor comment
- The following has some issues
 ## Support and contact details
Contact [Neville Kaundu](n3vd3v@gmail.com) for further help/support
 ### License
MIT
 Copyright (c)2018 **Neville Kaundu**