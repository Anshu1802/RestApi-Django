from rest_framework import serializers
from myapp.models import Company,Employee

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    # name=serializers.ReadOnlyField()               to only read the name and cannot edit the name field at any cost

    class Meta:
        model=Company
        fields="__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # name=serializers.ReadOnlyField()               to only read the name and cannot edit the name field at any cost

    class Meta:
        model=Employee
        fields="__all__"