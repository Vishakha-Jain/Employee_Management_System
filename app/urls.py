
from django.urls import path
from .views import *
urlpatterns = [
    path("",emp_Homepage,name="index"),
    path("add_emp/",add_Emp,name="add_Emp"),
    path("delete-emp/<int:id>/",delete_Emp,name="delete_emp"),
    path("update-emp/<int:id>/",update_Emp,name="update_emp"),
    path("update-success_emp/<int:id>/",update_Success_Emp,name="update-success_emp"),
    path("testimonials/",testimonials,name="testmonials"),
    path("feedback/",feedback,name="feedback"),

]