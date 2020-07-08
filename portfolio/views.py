from django.shortcuts import render,redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse  , HttpResponseRedirect
from .forms import ContactFroms

from .models import (
    HomeSlider,
    About,
    AboutPerformance,
    Service,
    Live_work,
    CaseWork,
    Contact,
    CompanyBrand,
    FQuestion,
    Blog
)

# Create your views here.

# Home Area
def index(request):
    #Home Section
    sliders=HomeSlider.objects.all()
    #About Section
    aboutUs=About.objects.get()
    aboutPerformance=AboutPerformance.objects.all()
    #Service Section
    serviceAll=Service.objects.all()
    #Live Work Section
    live_work=Live_work.objects.get()
    #Case Work Section
    caseWork=CaseWork.objects.all()
    #commnet slider section
    contactSlider=Contact.objects.all()
    #Brand Section
    companyBrand=CompanyBrand.objects.all()
    #FQ Section
    fQuestion=FQuestion.objects.all()
    #Blog Section
    blogs=Blog.objects.all()
    #Contact Section
    
    if request.method=='POST':
        form=ContactFroms(request.POST)

        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            selectOption=form.cleaned_data['selectOption']
            message=form.cleaned_data['message']
            recipients=['admin@example.com']
            try: 
                if name:
                    recipients.append(email)
                send_mail(email,selectOption,message,recipients)
            except BadHeaderError:
                return HttpResponse('ivalid header') 

            return redirect('send_success')
    else:
        form=ContactFroms()

    context={
        'sliders':sliders,
        'aboutUs':aboutUs,
        'aboutPerformance':aboutPerformance,
        'serviceAll':serviceAll,
        'live_work':live_work,
        'caseWork':caseWork,
        'contactSlider':contactSlider,
        'companyBrand':companyBrand,
        'fQuestion':fQuestion,
        'blogs':blogs,
        'form':form,
    
       
    }
    return render(request,'index.html',context)


def send_success(request):
    return HttpResponse('thanks you for you email ^_^')


