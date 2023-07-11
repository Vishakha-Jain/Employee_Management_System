from django.contrib import admin
from .models import *
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    # this is the list which we want to display when django admin login
    list_display=('name','working','emp_id')
    # this the variable which is used to make different fields as a editable
    list_editable=('working',)
    # there ia search field too
    search_fields=('name',)
    # list filter is used
    list_filter=('working',)

# inherit the class 
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)