Students Exams
==============

Simple Django project used as backend for an [Android Workshop][2] taken on [University of Perugia][1] (Computer Science department).

How to run it locally?
======================

Just run it as any other django app:

* Use mkvirtualenv to create a new python virtualenv (`python 2.7.x`)
* Use pip (inside virtualenv) to download all requirements (`pip install -r requirements.txt`)
* Sync your database (it uses sqlite3 as default backend) with (`python manage.py syncdb`) and create your admin user
* Run server! (`python manage.py runserver`)
* Access to `http://localhost:8000/admin`

Branches
========

Two branches are available:

* `master`: it is suitable to run it locally
* `heroku`: it is suitable to run it on [Heroku cloud service][3]

[1]: http://www.dmi.unipg.it
[2]: https://github.com/emanuele-palazzetti/android-workshop-slides
[3]: https://www.heroku.com/
