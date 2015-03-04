{% if false %}
# Azure Django Scaffold

## About

Scaffold for running Django 1.7 on Azure Websites. Includes common features such as:

* Redis cache
* Storage using Azure's Blob Storage
* PIL
* PyCrypto
* Grunt tasks for compiling SASS and versioning static files

## Setting up your project

* `mkvirtualenv yourproject`
* `workon yourproject`
* `django-admin.py startproject yourproject --template https://github.com/potatolondon/azure-django-scaffold/archive/master.zip --name .gitignore,Gruntfile.js,base.html,README.md,dev-only-package.json`
* `cd yourproject`
* `./start_project.sh`
* `rm start_project.sh`
* `grunt`
* In other tab, run `python manage.py runserver --settings=yourproject.settings.local`
* Commit as your initial commit!

## Deploying

You need a Python Azure Website, storage account, Redis cache and SQL database. Use the same name as used in the setup steps above for your Website and storage account. Define the following environment variables:

* DJANGO_SETTINGS_MODULE
* SECRET_KEY
* DB_HOST
* DB_USER
* DB_PASSWORD
* REDIS_HOST
* REDIS_PASSWORD
* BLOBSTORE_ACCOUNT_NAME
* BLOBSTORE_ACCOUNT_KEY


{% endif %}
# {{ project_name|title }}

## About

Put your project description here.
