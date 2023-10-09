from django.shortcuts import render, get_object_or_404


# Create your views here.

from .models import Major

def major_list(request):
    majors = Major.objects.all()
    major_list=[]
    for major in majors:
        major_list.append({'major': major})
    context = {'major_list':major_list}
    return render(request,'major_list.html', context)

def major_course(request, id):
    major = get_object_or_404(Major, id=id)
    core = major.core.all()
    context = {"major":major,
               "core":core}
    return render(request, "major_list.html",context)