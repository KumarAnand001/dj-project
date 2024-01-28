from django.shortcuts import render
from testapp.models import *

# Create your views here.
def index(request):

    return render(request, 'testapp/index.html')

def hydView(request):

    jobs_list = HydJobs.objects.order_by()
    dict = {'jobs_list' : jobs_list}
    return render(request, 'testapp/hydjobs.html', context=dict)

def bloreView(request):

    # jobs_list = HydJobs.objects.order_by()
    # dict = {'jobs_list' : jobs_list}
    return render(request, 'testapp/blorejobs.html')

def chennaiView(request):

    # jobs_list = HydJobs.objects.order_by()
    # dict = {'jobs_list' : jobs_list}
    return render(request, 'testapp/chennaijobs.html')

def puneView(request):

    # jobs_list = HydJobs.objects.order_by()
    # dict = {'jobs_list' : jobs_list}
    return render(request, 'testapp/punejobs.html')