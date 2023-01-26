# This project was setup with pipenv to manage the dependencies rather than pip.
So run PIPENV INSTALL (to install all the project's dependencies) after cloning the project
and pipenv shell to activate the virtual environment. Don't forget to select the python
interpreter created by pipenv via vs code's command palette and use it as the interpreter.


# Users Details Created for this project

## User 1
### Username: admindjango
### Password: employee1@123!

## User 2
### Username: portipher
### Password: open-sesame09


# API Endpoints
## For models and their views
1. For reserve a table functionality: http://127.0.0.1:8000/tables/
2. Get and Post request for all menu items http://127.0.0.1:8000/restaurant/menu
3. Get/PUT/PATCH/DELETE request for a single menu item http://127.0.0.1:8000/restaurant/menu/1

## For User Registration and authentication
1. GET and Post request for users and to register a new user http://127.0.0.1:8000/auth/users/
2. Post request To Login a user and obtain token http://127.0.0.1:8000/auth/token/login/
3. Post request To Logout user and destroy their token http://127.0.0.1:8000/auth/token/logout/


#Testing
## As per the course instructions, the unit tests for the models and views are in a seperate
tests folder. The location of the tests require a slight modification in the command to run the
tests. The command in this case is:
                                python manage.py test tests.

