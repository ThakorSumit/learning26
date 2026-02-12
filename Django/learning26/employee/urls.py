from django.urls import path
from . import views

urlpatterns = [
    path("employeelist/",views.employeelist,name="employeelist"),
    # path("employeefilter/",views.employeefilter),
    path("createemployee/",views.createEmployee,name="createemployee"),
    path("createcourse/",views.createcourse),
    path("createcollege/",views.createcollege),
    path("createproduct/",views.createproduct),
    path("deleteemployee/<int:id>",views.deleteemployee,name="deleteemployee"),
    path("filter/<str:order>",views.employeefilter,name="employeefilter"),

]