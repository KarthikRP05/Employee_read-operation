from django.db import models

class Department(models.Model):
    dept_id = models.IntegerField(unique=True)
    dept_name = models.CharField(max_length=100,db_index=True)

    def __str__(self):
       return self.dept_name

class Employees(models.Model):
    emp_id = models.IntegerField(unique=True)
    emp_name = models.CharField(max_length=100,db_index=True)
    emp_dept = models.CharField(max_length=100)
    emp_dob = models.DateField()
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
       return str(self.emp_id)

class Salary(models.Model):
    sal_id = models.IntegerField(unique=True)
    emp_id = models.ForeignKey(Employees, on_delete=models.CASCADE)
    dept_name = models.ForeignKey(Department,max_length=100,db_index=True,on_delete=models.CASCADE)
    sal_net = models.IntegerField()

    def __str__(self):
       return str(self.sal_id)  

       