from django.shortcuts import render
from django.db.models import Count
from testapp.models import Employees,Department,Salary

def show(request):
    employees = Employees.objects.all()
    department = Department.objects.all()
    salary = Salary.objects.all()
    d = Department.objects.all()


    dept_count = Employees.objects.values('dept_id__dept_name') \
    .annotate(total=Count('emp_id')) \
    .order_by('total')

    return render(request,"show.html",{'employee':employees,'department':department,'salary':salary,
    'dept_count':dept_count})


