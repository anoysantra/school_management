from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import AcademicSession
from .forms import AcademicSessionForm

# Create your views here.

def SessionAdd(request):
    sessions=AcademicSession.objects.all()
    if request.method=='POST':
        form=AcademicSessionForm(request.POST)
        print(request.POST)

        if form.is_valid():
            sessions_check=form.cleaned_data['session_name']

            for e in sessions:
                if sessions_check==e.session_name:
                    return HttpResponse("Academic Session Present")

            print("Form Valid Sesssion")

            form.save()
            return redirect('class_list')

    else:
        form=AcademicSessionForm()

    return render(request,'session_add.html',{'form':form})

def SessionList(request):

    sessions = AcademicSession.objects.all()
    return render(request, 'session_list.html',{'sessions': sessions})



def SessionUpdate(request,session_name):
    instance = get_object_or_404(AcademicSession, session_name=session_name)
    print(instance)
    sessions=AcademicSession.objects.all()

    if request.method == 'POST':
        form = AcademicSessionForm(request.POST, instance=instance)
        print("New Data : ", request.POST )

        if form.is_valid():               
                session_check=form.cleaned_data['session_name']
                startdate_check=form.cleaned_data['start_date']
                enddate_check=form.cleaned_data['end_date']

                for e in sessions:
                    if session_check == e.session_name and startdate_check == e.start_date and enddate_check == e.end_date:
                        return HttpResponse("Session Already Present.Cannot be updated Error")
                    
                form.save()
                return redirect('class_list')
        
    else:
        form = AcademicSessionForm(instance=instance)

    return render(request, 'session_update.html', {'form': form, 'instance': instance})

def SessionDelete(request,session_name):
    session=get_object_or_404(AcademicSession,session_name=session_name)
    if request.method == 'POST':
        session.delete()
        return redirect('class_list')
    
    return render(request, 'session_delete.html', {'session':session})   

                



