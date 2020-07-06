from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class HomeSlider(models.Model):
    title=models.CharField(max_length=400)
    image=models.FileField(upload_to='home')
    subtitle=models.CharField(max_length=300)
    description=models.TextField()

    def __str__(self):
        return self.title


class About(models.Model):
    subtitle=models.CharField(max_length=400)
    description=models.TextField()
    
    def __str__(self):
        return self.subtitle

class AboutPerformance(models.Model):
    about_title_help=models.CharField(max_length=400)
    about_image=models.FileField(upload_to='about')
    about_description=models.TextField()
    def __str__(self):
        return self.about_title_help


class Service(models.Model):
    title=models.CharField(max_length=400)
    subtitle=models.CharField(max_length=400)
    about_image=models.FileField(upload_to='service')
    description=models.TextField()

    def __str__(self):
        return self.title


class Live_work(models.Model):
    title=models.CharField(max_length=400)
    subtitle=models.CharField(max_length=400)
    video_link=models.URLField(max_length=500)

    def __str__(self):
        return self.title


class CaseWork(models.Model):
    title=models.CharField(max_length=400)
    image=models.FileField(upload_to='case')
    read_more=models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Contact(models.Model): 
    title=models.CharField(max_length=400)
    description=models.TextField()
    profession=models.CharField(max_length=400)
    name=models.CharField(max_length=400)
    email=models.EmailField( max_length=254)
    subject=models.CharField(max_length=400)
    message=models.TextField()

    def __str__(self):
        return self.title


class CompanyBrand(models.Model):
    company_logo=models.FileField(upload_to='brand')


class FQuestion(models.Model):
    question=models.CharField(max_length=400)
    answer=models.TextField()

    def __str__(self):
        return self.question


class Blog(models.Model):
    image=models.FileField(upload_to='blog')
    title=models.CharField(max_length=400)
    comments=models.CharField(max_length=400)
    admin_name=models.ForeignKey(User, on_delete=models.CASCADE)
    read_more=models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Footer(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    submit_email=models.EmailField(max_length=254)
    address=models.CharField(max_length=200)
    number=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    privacy=models.TextField()
    term=models.TextField()
    copy_right=models.CharField(max_length=400)

    def __str__(self):
        return self.title
    

    