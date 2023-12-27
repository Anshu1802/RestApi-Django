from django.shortcuts import render
from rest_framework import viewsets
from myapp.models import Company,Employee
from myapp.serializer import CompanySerializer,EmployeeSerializer



class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmployeeSerializer
