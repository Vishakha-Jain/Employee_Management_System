from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def emp_Homepage(request):
    emps=Emp.objects.all()
    return render(request,"index.html",{'emps':emps})

def add_Emp(request):
    if request.method == "POST":
        # data fetch
        name=request.POST["emp_name"]
        emp_id=request.POST["emp_id"]
        email=request.POST["emp_email"]
        phone=request.POST["emp_phone"]
        address=request.POST["emp_address"]
        working=request.POST.get("emp_working") 
        # the get method of request.POST is used for not getting any error
        department=request.POST["emp_department"]

        if working is None:
            working_bool=False
        else:
            working_bool=True
        # create model object and set data
        e=Emp.objects.create(name=name,emp_id=emp_id,email_id=email,phone=phone,address=address,working=working_bool,department=department)

        # save the object


        print("data is coming")
        return redirect("/")
    
    # this below two lines are used for when form is creted using model and you have to crerate form in html,then this two line codes are used.
    # form=Empform()
    # return render(request,"add_emp.html",{'form':form})


    return render(request,"add_emp.html")


def delete_Emp(request,id):
    print(id)
    e=Emp.objects.get(pk=id)
    e.delete()
    return redirect("/")

def update_Emp(request,id):
    print(id)
    emp=Emp.objects.get(id=id)
    print(emp.department)
    return render(request,"update_emp.html",{'emp':emp})

def update_Success_Emp(request,id):
    if request.method=="POST":
        emp=Emp.objects.get(id=id)
        emp.name=request.POST["emp_name"]
        emp.emp_id=request.POST["emp_id"]
        emp.email=request.POST["emp_email"]
        emp.phone=request.POST["emp_phone"]
        emp.address=request.POST["emp_address"]
        working=request.POST.get("emp_working") 
        # the get method of request.POST is used for not getting any error
        emp.department=request.POST["emp_department"]

        if working is None:
            emp.working=False
        else:
            emp.working=True
        emp.save()
        print(emp.id)
        return redirect("/")

def testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,"testimonials.html",{'testi':testi})

def feedback(request):
    if request.method=="POST":
        form=FeedbackForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            name=form.cleaned_data['name']
            feedback=form.cleaned_data['feedback']
            f=Feedback.objects.create(email=email,name=name,feedback=feedback)
            return redirect("/")
            print("data saved")
        else:
            return render(request,"feedback.html",{'form':form})
    else:
        form=FeedbackForm()
        return render(request,"feedback.html",{'form':form})