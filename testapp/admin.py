from django.contrib import admin
from testapp.models import HydJobs, BloreJobs, ChennaiJobs, PuneJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):

    list_display = [
        
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]

class BloreJobsAdmin(admin.ModelAdmin):

    list_display = [
        
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]

class ChennaiJobsAdmin(admin.ModelAdmin):

    list_display = [
        
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]

class PuneJobsAdmin(admin.ModelAdmin):

    list_display = [
        
        'date',
        'company',
        'title',
        'eligibility',
        'address',
        'email',
        'phonenumber'
    ]


admin.site.register(HydJobs, HydJobsAdmin)
admin.site.register(BloreJobs, BloreJobsAdmin)
admin.site.register(ChennaiJobs, ChennaiJobsAdmin)
admin.site.register(PuneJobs, PuneJobsAdmin)