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
    #About Section
    aboutUs=About.objects.get()
    aboutPerformance=AboutPerformance.objects.all()
    #Service Section
    serviceAll=Service.objects.all()
    #Live Work Section
    live_work=Live_work.objects.get()
    #Case Work Section
    caseWork=CaseWork.objects.all()

    context={
        'sliders':sliders,
        'aboutUs':aboutUs,
        'aboutPerformance':aboutPerformance,
        'serviceAll':serviceAll,
        'live_work':live_work,
        'caseWork':caseWork,
    }
    return render(request,'index.html',context)
