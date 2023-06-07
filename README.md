# Perfume online marketplace

Perfume online marketplace built using [Django](https://www.djangoproject.com/) and [Angular](https://angular.io/). The database is local made using
[PostgreSQL](https://www.postgresql.org/). It features a list of perfumes that can be viewed, the users being able to write comments about them. It features authentication, authorization, shopping cart, checkout.

Deployed at https://django-perfume.herokuapp.com/admin using [Heroku](https://dashboard.heroku.com/).
Databased deployed using [Google Cloud](https://cloud.google.com/).

# Front-end

Please go to https://github.com/redikus3q/perfume-frontend to pull and check out the back-end.

# Back-end

Made using [Django 4.1](https://docs.djangoproject.com/en/4.1/releases/4.1/) with [Django REST Framework](https://www.django-rest-framework.org/) for handling REST requests
and [Django simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for better authentication and authorization.

## Prerequisites

```bash
pip install -r requirements.txt
```

## Installation

[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or [download](https://www.itprotoday.com/development-techniques-and-management/how-do-i-download-files-github) the application.

## Usage

Use the following command in the main directory of the back-end part, in our case /backend. The back-end will be accessible at [127.0.0.1:8000](http://127.0.0.1:8000/).

```bash
python manage.py runserver
```
