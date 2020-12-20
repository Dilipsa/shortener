django project/api to shorten a url

to run project
================
clone the repo
cd shortener
python3 -mvenv venv/                virtualenv venv
source venv/bin/activate/           source venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver

admin
============
username : dilip
password : password@123






api endpoints
=======================================================
create shottened urls------->http://127.0.0.1:8000/api/

list of all urls------------>http://127.0.0.1:8000/api/all-urls/

delete urls ---------------->http://127.0.0.1:8000/api/delete-url/<pk>/

redirect urls--------------->http://127.0.0.1:8000/api/<slug>/

fetch original url---------->http://127.0.0.1:8000/api/<slug>/

