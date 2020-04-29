Project Installation
------------------------------------------

This project requies virtualenv and python installed on the host and use the below commands to run the project


virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver


Autogenerate class diagram with django extension
------------------------------------------
python manage.py graph_models -a -o myapp_models.png


Executing Test Cases
------------------------------------------
python manage.py test
