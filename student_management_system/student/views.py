from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status  
from .models import Student 
from .serializers import StudentSerializer 
from django.shortcuts import get_object_or_404  

# Create your views here.

class StudentView(APIView):
    def get(self, request):
        result = Student.objects.all()
        serializers = StudentSerializer(result, many=True)
        return Response({'status':'success', "students":serializers.data}, status=200)

    def post(self, request):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', "students":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status':'error', "students":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        result = Student.objects.get(id=id)
        if id:
            serializer = StudentSerializer(result, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'success', "students":serializer.data})
        else:
            return Response({'status':'error', "students":serializer.errors})  


@api_view(['GET', 'DELETE'])
def GetStudentById(request, pk):
    try:
        students = Student.objects.get(pk=pk)
    except Students.DoesNotExist:
        error = {'status':'400', 'message':'NOT FOUND'}
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        students.delete()
        return Response({'status': 'student deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


