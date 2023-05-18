from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    roll_no = serializers.IntegerField()
    address = serializers.CharField(max_length=100, required=True)
    mobile_no = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Student
        fields=('__all__')