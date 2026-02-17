from .models import employee
from django.urls import path
from . import views

urlpatterns = [
    path("employeelist/",views.employeelist,name="employeelist"),
    path("createemployee/",views.createEmployee,name="createemployee"),
    path("createcourse/",views.createcourse,name="createcourse"),
    path("createcollege/",views.createcollege,name="createcollege"),
    path("createproduct/",views.createproduct,name="createproduct"),
    path("deleteemployee/<int:id>",views.deleteemployee,name="deleteemployee"),
    path("filter/<str:order>",views.employeefilter,name="employeefilter"),
    path("updateemployee/<int:id>",views.updateemployee,name="updateemployee"),

]