from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . models import Employee
from . serializers import EmployeeSerializer
from django.http import Http404
from blogs.pagination import CustomPagination
from rest_framework import mixins, generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .filters import EmployeeFilter
from django_filters.rest_framework import DjangoFilterBackend
# #class based views
"""
class Employees(APIView):
    def get(self,request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
class EmployeesDetails(APIView):
    def get_object(self,pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request ,pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request , pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""

# Mixins 
# generics gives get, post, put and delete methods this handles request and response
# mixing gives list create retrive update and destroy methods this handles core functionalities
""""
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 

    def get(self,request):
        return self.list(request)
    
    def post (self,request):
        return self.create(request)
    
class EmployeesDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)
"""

# Generics 
# ListAPIView , CreateAPIView , RetrieveAPIView, DestroyAPIView and UpdateAPIView
# ListCreateAPIView and RetrieveUpdateDestroyAPIView
"""
class Employees(generics.ListAPIView, generics.CreateAPIView,):
    queryset = Employee.objects.all()
    serializer_class  = EmployeeSerializer


class EmployeesDetails(generics.RetrieveAPIView, generics.DestroyAPIView , generics.UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class  = EmployeeSerializer
    lookup_field = 'pk'

"""

# Viewsets
# list, create , retrieve , update and delete 

"""
class EmployeeViewset(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None):
        employee = get_object_or_404(Employee,pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
#ModelViewSets

# filtering example  filter backend to an individual View or ViewSet.
"""
class EmployeeViewset(viewsets.ModelViewSet):
    queryset =Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['designation']
    
"""
# filtering example using filterbackend in setting.py and custom filter
class EmployeeViewset(viewsets.ModelViewSet):
    queryset =Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    filterset_class = EmployeeFilter