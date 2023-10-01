from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Exams
from .forms import ExamForm

# Create your views here.

def ExamAdd(request):
    exams=Exams.objects.all()
    if request.method=='POST':
        form=ExamForm(request.POST)
        print(request.POST)

        if form.is_valid():
            exams_check=form.cleaned_data['exam_name']

            for e in exams:
                if exams_check==e.exam_name:
                    return HttpResponse("Academic Exam Present")

            print("Form Valid Sesssion")

            form.save()
            return redirect('class_list')

    else:
        form=ExamForm()

    return render(request,'exam_add.html',{'form':form})


def ExamList(request):

    exams = Exams.objects.all()
    return render(request, 'exam_list.html',{'exams': exams})



def ExamUpdate(request,exam_name):
    instance = get_object_or_404(Exams, exam_name=exam_name)
    print(instance)
    exams=Exams.objects.all()

    if request.method == 'POST':
        form = ExamForm(request.POST, instance=instance)
        print("New Data : ", request.POST )

        if form.is_valid():               
                exam_check=form.cleaned_data['exam_name']
                full_marks_check=form.cleaned_data['full_marks']

                for e in exams:
                    if exam_check == e.exam_name and full_marks_check==e.full_marks:
                        return HttpResponse("Exam Details Already Present.Cannot be updated Error")
                    
                form.save()
                return redirect('class_list')
        
    else:
        form = ExamForm(instance=instance)

    return render(request, 'exam_update.html', {'form': form, 'instance': instance})


def ExamDelete(request,exam_name):
    exam=get_object_or_404(Exams,exam_name=exam_name)
    if request.method == 'POST':
        exam.delete()
        return redirect('class_list')
    
    return render(request, 'exam_delete.html', {'exam':exam})   

                



