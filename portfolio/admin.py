from django.contrib import admin
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

# Register your models here.

admin.site.register(HomeSlider)
admin.site.register(About)
admin.site.register(AboutPerformance)
admin.site.register(Service)
admin.site.register(Live_work)
admin.site.register(CaseWork)
admin.site.register(Contact)
admin.site.register(CompanyBrand)
admin.site.register(FQuestion)
admin.site.register(Blog)
admin.site.register(Footer)
