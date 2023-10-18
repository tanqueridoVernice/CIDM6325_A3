from django.shortcuts import render, get_object_or_404


# Create your views here.

from .models import Major, Core

def welcome_view (request):
    return render(request, 'base.html')

def major_list(request):
    majors = Major.objects.all()
    major_list = []
    for major in majors:
        major_list.append({'major': major})
    context = {'majors':majors}
    return render(request,'major_list.html', context)

def core_list(request,pk):
    major = get_object_or_404(Major, pk=pk)
    cores = major.core_set.all()
    context = {'major':major,
               'cores':cores}
    return render(request,'course_list.html', context)