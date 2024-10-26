from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Department,Role,Employee
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render (request,'index.html')

def all(request):
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render (request,'all_emp.html',context)

def add(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        dept = request.POST['dept']
        phone = int(request.POST['phone'])
        hire_date = (request.POST['hire_date'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, role_id=role, dept_id=dept, phone=phone, hire_date=hire_date)
        new_emp.save()
        return render(request, 'add_success.html')
    elif request.method == "GET":
        return render (request,'add_emp.html')
    else:
        return HttpResponse("<h1>Employee has not been added</h1>")

def remove(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            if request.method == 'POST':
                emp_to_be_removed.delete()
                return render(request, 'remove_success.html')
            else:
                return render(request, 'confirm_remove_emp.html', {'employee': emp_to_be_removed})
        except Employee.DoesNotExist:
            return HttpResponse("<h2>Enter a valid Employee ID</h2>")
        
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    return render (request,'remove_emp.html',context)

def filter(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        dept = request.POST['dept']
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if role:
            emps = emps.filter(role__name__icontains=role)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        
        context={
        'emps':emps
    }
        return render (request,'all_emp.html',context)
    
    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An error occured')