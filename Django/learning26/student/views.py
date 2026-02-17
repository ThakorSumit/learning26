# Create your views here
from django.shortcuts import render,redirect
from .models import Student
from .form import StudentForm
 
def marks(request):
    return render(request,"student/marks.html")

def info(request):
    data={"name":"sumit","std":"10th","DOB":10-5,"result":80}
    return render(request,"student/info.html",data)

def faculty(request):
    data={'sub1':'Maths','teacher1':'Dr. Meera Nair',"qual1":"Ph.D. Mathematics",
          'sub2':'English','teacher2':'Piyush Patel',"qual2":"M.A. English  Literatuer",
          'sub3':'Science','teacher3':'Harish singh',"qual3":"Msc. Physics"
          }
    return render(request,"student/faculty.html",data)


def studentlist(request):
    data=Student.objects.all().order_by('id')
    return render(request,"student/studentlist.html",{'data':data})

def creatprofile(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form=StudentForm()
    return render(request,"student/creatprofile.html",{'form':form})

def deleteprofile(request,id):
    Student.objects.filter(id=id).delete()
    return redirect('studentlist')

def updateprofile(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form=StudentForm(instance=student)
    return render(request,"student/creatprofile.html",{'form':form})
    