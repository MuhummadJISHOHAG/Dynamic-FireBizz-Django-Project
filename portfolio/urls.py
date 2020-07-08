from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="indexPage" ),
    path('success/' , views.send_success , name='send_success'),
]

# python manage.py migrate
# python manage.py makemigrations
# python manage.py runserver