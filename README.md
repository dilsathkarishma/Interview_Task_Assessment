

Features

Simple web interface to view or manage shop items.
Backend built using Python Django.
Database to store shops data using MySql
Docker support for easy deployment.
Git-tracked project for version control.
Prerequisites: To work on this project, we need to install following in our machine,

python 3.10
django 3.2.18
djangorestframework 3.13.1
Virtual Environment It is suggested to have a dedicated virtual environment for each Django project, and one way to manage a virtual environment is venv, which is included in Python. The name of the virtual environment is your choice, in this tutorial we will call it myworld.

Type the following in the command prompt, remember to navigate to where you want to create your project:

Windows: python -m venv "Env_name"

Ios/Linux: python3 -m venv "Env_name"

Quick Start:

Your directory tree should be like this,

├── coffeshop_project
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── swagger_service
│   ├── urls.py
│   ├── wsgi.py
├── logs
├── shop_app
│   ├── migrations
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializer.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
├── app.py
├── README.md
└── requirements.txt




Install Dependencies:

   $pip install -r requirements.txt
Run Locally:

   $python app.py runserver 0.0.0.0:8000
