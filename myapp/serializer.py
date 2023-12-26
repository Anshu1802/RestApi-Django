from rest_framework import serializers
from myapp.models import Company

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
