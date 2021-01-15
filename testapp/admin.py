from django.contrib import admin
from .models import Employees,Department,Salary
# Register your models here.
admin.site.register(Department)
admin.site.register(Employees)
admin.site.register(Salary)

