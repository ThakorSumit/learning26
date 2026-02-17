from django.urls import path
from . import views
urlpatterns = [
    path('marks/',views.marks),
    path('info/',views.info),
    path('teachers/',views.faculty),
    path('studentlist/',views.studentlist,name='studentlist'),
    path('creatprofile/',views.creatprofile,name='creatprofile'),
    path('deleteprofile/<int:id>/',views.deleteprofile,name='deleteprofile'),
    path('updateprofile/<int:id>/',views.updateprofile,name='updateprofile'),
]