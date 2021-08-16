# Campus_Placement_Prediction
Predicting student will get campus placement or not 

If you want to use this. first download the code go to command prompt create a virtual enviornment in python

> virtualenv name 

<b>Install all the dependecies which is in the file requirement.txt</b>
> python manage.py runserver 

Open your browser type 127.0.0.1:8000 
Site will be live on your local system
<h1> To Deploy Django Project to Heroku </h1>

1.	Create Heroku Account : https://www.heroku.com/

2.	Download and Install Git : https://git-scm.com/downloads
3.	Download and Install Heroku CLI : https://devcenter.heroku.com/articles/heroku-cli#download-and-install
4.	Open Terminal
5.	Login into Heroku CLI. Run below command it will open Browser then Click on Login
 > heroku login 
6.	Create Repo for Project
  > git init
7.	Add All Files to Repo
  > git add . 
8.	Commit All Changes
  > git commit -m "any comment"
9.	Create an App using Dashboard or Shell (I am creating using Shell)
  > heroku create heroku_app_name
10.	Set Repo
 > heroku git:remote -a heroku_app_name
11.	Install gunicorn or waitress - This will be our production server as we can not use development server which we were using by runing python manage.py runserver. Waitress is meant to be a production-quality pure-Python WSGI server with very acceptable performance. For More: https://docs.pylonsproject.org/projects/waitress/en/latest/
 > pip install waitress
12.	Run wsgi.py file using waitress to test everything works fine on Local Machine (Before Pushing to Heroku)

> waitress-serve --port=8000 inner_project_folder_name.wsgi:application

13.	You will get a link in terminal just open it. If everything works then you will be able to see your project running on Web Browser
14.	If you get an error: Disallowed Host Invalid HTTP_HOST header then do below change in Django's Settings.py file and re-run wsgi.py file as Step 12
 ```
 ALLOWED_HOSTS = ['*']
 ```
15.	Create a file named Procfile then write below code in the file
```
  web: waitress-serve --port=8000 inner_project_folder_name.wsgi:application
  ```
16.	Run below command - This will use Procfile to run the project. You will see an URL open it if everything file you will see project in browser
  > heroku local
17.	Now go to your Django project's settings and do below change
```
  DEBUG = False
  
  ALLOWED_HOSTS = ['heroku_app_name.herokuapp.com']
  ```
As you have created an Heroku App so you have your app url e.g. https://heroku_app_name.herokuapp.com/ You can find it follwoing Heroku's Dashboard -> Setting

18.	If you have static files must include STATIC_ROOT in Django's settings.py file
```
  STATIC_ROOT = BASE_DIR / "static"
```
19.	Bundle all requirements
 > pip freeze > requirements.txt
20.	Make sure you have changed 

_web: waitress-serve --port=8000 inner_project_folder_name.wsgi:application_ 
to
```
web: waitress-serve --port=$PORT inner_project_folder_name.wsgi:application
```
in Procfile before pushing to heroku
21.	Run below command


> git add . 

> git commit -m "any comment"

> git push heroku master 

22.	Done


