from django.shortcuts import render,HttpResponse,redirect
from .models import employee,course,college,ShopProduct
from .form import EmployeeForm,CourseForm,collegeform,ProductForm
# Create your views here.
def employeelist(request):
    emp=employee.objects.all().order_by("id").values()
    return render(request,"employee/employee.html",{'emp':emp})

# def employeefilter(request):
#     emp=employee.objects.all().values()
#     emp2=employee.objects.filter(age__exact=23).values()
#     emp3=employee.objects.filter(post="Data Scientist").values()
#     emp4=employee.objects.filter(salary__gt=29000).values()
#     emp5=m=employee.objects.filter(name__icontains="It").values()
#     emp6=employee.objects.filter(age__range=(25,30)).values()
#     emp7=employee.objects.order_by("salary").values()
#     print("emp2",emp2)
#     print("emp3",emp3)
#     print("emp4",emp4)
#     print("emp5",emp5)
#     print("emp6",emp6)
#     print("emp7",emp7)

    # return HttpResponse("Employee filter successfully")

def createEmployee(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("employeelist")
    else:
        form=EmployeeForm()
        return render(request,"employee/createemploye.html",{'form':form})

def createcourse(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Course created successfully")
    else:
        form=CourseForm()
        return render(request,"employee/createcourse.html",{'form':form})

def createcollege(request):
    if request.method=="POST":
        form=collegeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("college created successfully")
    else:
        form=collegeform()
        return render(request,"employee/createcollege.html",{'form':form})

def createproduct(request):
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product added successfully")
    else:
        form=ProductForm()
        return render(request,"employee/createproduct.html",{'form':form})


def deleteemployee(request,id):
       emp=employee.objects.get(id=id)
       emp.delete()
       return redirect("employeelist")


def employeefilter(request,order):
    if order=='1':
        emp=employee.objects.order_by("age").values()
    if order=='2':
        emp=employee.objects.order_by("-age").values()
    return render(request,"employee/employee.html",{'emp':emp})


def updateemployee(request,id):
    emp=employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('employeelist')
    else:
        form=EmployeeForm(instance=emp)
        return render(request,"employee/updateemployee.html",{'form':form})

