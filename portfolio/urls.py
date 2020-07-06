from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="indexPage" )
]

# python manage.py migrate
# python manage.py makemigrations
# python manage.py runserver