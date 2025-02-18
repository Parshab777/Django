<!-- Install virtual environment -->
pip install virtualenv


<!-- create virtual environment -->
virtualenv environment__name 
python -m virtualenv environment__name
(From two anyone can be used.)

<!-- Activate virtual environment -->
env\Scripts\activate
(This code should be used in the command prompt.)

<!-- Install django -->
pip install django

<!-- freeze the packages -->
pip install -r requirements.txt

<!-- Create django Project -->
django-admin startproject project__name .  {"." after using this . the project_name file directly form}


<!-- start server -->
python manage.py runserver


<!-- Create app -->
pythom manage.py startapp todo

<!-- Migration file -->
python manage.py makemigrations

<!-- create db table -->
python manage.py migrate


<!-- For interactive console -->
python manage.py shell 
{For this we should be in the project directory.}


<!-- Create Data -->
Model_name.objects.create(field = "", field2 = ""...)

<!-- View all Data-->
Model_name.objects.all()

<!-- View Single Data -->
a = Model_name.objects.get(Field_name=....)

<!-- Update Data -->
a.field_name = "new value"
a.save()
But we must have aaisgn the object value to a.


<!--  Delete Data -->
Model_name.objects.get(Field_name = "...").delete()
a.delete()


<!-- Filter Data -->
Model_name.objects.filter(field_name = "value")

<!-- Count Data -->
Model_name.objects.filter(field_name = "value").count()