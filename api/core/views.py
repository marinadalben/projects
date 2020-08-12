from rest_framework import generics, response, status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from core.models import Employee
from core.serializers import EmployeeSerializer


class EmployeeCreateView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all employees.

    post:
    Create a new employee.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get, put, patch and delete 
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
