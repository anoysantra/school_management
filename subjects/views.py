from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Subjects
from .forms import SubjectsForm
from classes.models import Classes

# Create your views here.


def SubjectsAdd(request,class_name):
    classes = Classes.objects.get(class_name=class_name)
    subjects=Subjects.objects.filter(class_name=class_name)  #debug
    print(subjects)  

    print("Class is:",classes)
    
    if request.method=='POST':
        print(request.POST)
        form=SubjectsForm(request.POST)
        
        if form.is_valid():
            subject_check=form.cleaned_data['subjects_name'] #debug
            print(subject_check)

            for e in subjects:
                if subject_check == e.subjects_name:
                    return HttpResponse("Subject Already Present. Error")
            
            print(type(subject_check))
            print("Its valid")
            form.instance.class_name = classes
            form.save()
            return redirect('class_list')
        
    else:
        print("Not Valid")
        form=SubjectsForm()

    return render(request,'subjects_add.html',{'classes':classes , 'form':form})

def SubjectsList(request,class_name):
    classes=get_object_or_404(Classes,class_name=class_name)
    subjects=Subjects.objects.filter(class_name=classes).values()
    print("Subjects is: ",subjects)
    return render(request, 'subjects_list.html', {'classes': classes, 'subjects': subjects})


def SubjectsUpdate(request,class_name,subjects_name):

    classes=get_object_or_404(Classes,class_name=class_name)
    subjects=get_object_or_404(Subjects, class_name=classes, subjects_name=subjects_name)
    c_subject=Subjects.objects.filter(class_name=class_name)

    if request.method=='POST':
        form=SubjectsForm(request.POST, instance=subjects)

        if form.is_valid():
            class_name_check=form.cleaned_data['class_name']
            subject_name_check=form.cleaned_data['subjects_name']

            if class_name_check!=classes.class_name:
                return HttpResponse("Keep class similar")
            
            for e in c_subject:
                if subject_name_check==e.subjects_name:
                    return HttpResponse("<h1> Subject already there</h1>")

            form.save()
            return redirect('class_list')
        
    else:
        form=SubjectsForm()

    return render(request, 'subjects_update.html', {'form': form, 'classes': classes, 'subjects':subjects})

def SubjectsDelete(request,class_name,subjects_name):
    classes=get_object_or_404(Classes,class_name=class_name)
    subjects=get_object_or_404(Subjects, class_name=classes, subjects_name=subjects_name)
    #subjects=Subjects.objects.filter(class_name=classes, subjects_name=subjects_name)
    if request.method == 'POST':
        subjects.delete()
        return redirect('class_list')
    
    return render(request, 'subjects_delete.html', {'classes':classes, 'subjects':subjects})

