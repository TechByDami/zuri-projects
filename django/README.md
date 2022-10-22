# Django
Django is one of the most popular (if not the most popular) high-level free and open-source Python web framework

## Why Django
There are so many reasons to pick django, and I'll mention a few:
* **It is fast** - Django helps take applications from concept to completion as quickly as possible.
* **It is secure** - Django framework does not joke with security. You need a .env to protect your file to even push to GitHub. In itself, django helps developers avoid many common security mistakes.
* **It is scalable** - With django it is easy to scale and expand projects 

## My Projects
As part of my requirements to pass my Fullstack Frontend Program with [Zuri](https://training.zuri.team/), I have completed to following projects:

1. [songcrud](https://github.com/B-Akapo/zuri-projects/tree/main/django/songcrud) - A music app

## Creating a Django Project
Installing Django is quite easy. Let's look at the steps. 

* **Step-1** - Ensure you have the latest version of [Python](https://python.org/downloads/)
* **Step-2** - When Installing Django on your system ensure you tick "ADD TO PATH" or you won't be able to use pip
* **Step-3** - Install **pipenv**. pip is a dependency management tool used installing application dependencies in a virtual environment
````
pip install pipenv
````
* **Step-4** - Create a directory and *cd* into it. Note if you don't know Git, GitHub and Terminal, you can learn from [amigoscode](https://www.youtube.com/c/amigoscode)
````
mkdir <name_of_directory>
cd <name_of_directory>
````
* **Step-5** - Create a virtual environment and install django 
````
pipenv install django
````
* **Step-6** - In your virtual environment, you need to run a virtual terminal.
````
pipenv shell
````
* **Step-7** - Now you can create your project in this virtual environment.
````
django-admin startproject <name_of_project> .
````
* **Step-8** - YEP. You have created your project now you can run it. 
````
python manage.py runserver
````