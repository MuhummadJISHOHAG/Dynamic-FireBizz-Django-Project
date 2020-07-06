from django.shortcuts import render
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
    Blog,
    Footer
)

# Create your views here.

# Home Area
def index(request):
    sliders=HomeSlider.objects.all()
    aboutUs=About.objects.get()
    aboutPerformance=AboutPerformance.objects.all()


    context={
        'sliders':sliders,
        'aboutUs':aboutUs,
        'aboutPerformance':aboutPerformance
    }
    return render(request,'index.html',context)
