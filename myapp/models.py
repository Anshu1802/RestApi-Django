from django.db import models

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(
                                                  ('IT','IT'),
                                                  ('Non IT','Non IT'),
                                                  ('CA','CA')))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.IntegerField()
    about=models.CharField(max_length=100)
    position=models.CharField(max_length=50,choices=(
                                                    ('Tfo','Tfo'),
                                                    ('Master','Master'),
                                                    ('Karigar','Karigar'),
                                                    ('Cleaner','Cleaner'),
                                                    ('New','New'),
                                                    ('Expert','Expert')
                                                    
                                                    ))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
# this is the forign key if we delte the employee name, then all data will be deleted
    