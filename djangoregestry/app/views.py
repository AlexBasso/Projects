from .serializers import SchoolSerializer, SchoolClassSerializer, StudentSerializer,UserSerializer
from .models import School, ScClass, Student
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import redirect
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions



"""  SchoolAPI  """

class SchoolList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_list.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        queryset = School.objects.all()
        sort = School.objects.values('schoolName').distinct()
        return Response({'schools': queryset, 'sort': sort})



class SchoolCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_create.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request):
        serializer= SchoolSerializer
        return Response({'serializer':serializer})

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('tmp_school-list')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SchoolDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_detail.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        school = get_object_or_404(School.objects.only('id', 'schoolName'), pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = SchoolSerializer(school, context=serializer_context)
        return Response({'serializer': serializer, 'school': school})

    def post(self, request, pk):
        school = get_object_or_404(School.objects.only('id', 'schoolName'), pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = SchoolSerializer(school, data=request.data, context=serializer_context)

        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': school})
        serializer.save()
        return redirect('tmp_school-list')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SchoolDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tmp_school_delete.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk):
        school = School.objects.filter(id = scpk)
        return Response({'school': school})

    def post(self, request, scpk):
        school = School.objects.filter(id = scpk)
        school.delete()
        return redirect('tmp_school-list')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""  ClassAPI  """

class SchoolClassList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_list.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk):
        queryset1 = School.objects.filter(id=scpk)
        queryset = ScClass.objects.filter(school__id=scpk)
        return Response({'schoolclasses': queryset, 'scpk': queryset1 })


class SchoolClassDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_detail.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk, clpk):
        queryset1 = School.objects.filter(id=scpk)
        scClass = get_object_or_404(ScClass, pk=clpk)
        serializer_context = {
            'request': request,
        }
        serializer = SchoolClassSerializer(scClass, context=serializer_context)
        return Response({'serializer': serializer, 'school': scClass, 'scpk': queryset1 })

    #scClass = ScClass.objects.filter(id=pk)
    def post(self, request, scpk, clpk):
        queryset1 = School.objects.filter(id=scpk)
        scClass = get_object_or_404(ScClass, pk=clpk)
        serializer_context = {
            'request': request,
        }
        serializer = SchoolClassSerializer(scClass, data=request.data, context=serializer_context)
        if not serializer.is_valid():
            print('in an if statement')
            return Response({'serializer': serializer, 'school': scClass, 'scpk': queryset1})
        serializer.save()
        return redirect('school_class-list', scpk=scpk)


class SchoolClassDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_delete.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk, clpk):
        queryset1 = School.objects.filter(id=scpk)
        scClass = get_object_or_404(ScClass, pk=clpk)
        return Response({'school': scClass, 'scpk': queryset1})

    def post(self, request, scpk, clpk):
        scClass = get_object_or_404(ScClass, pk=clpk)
        scClass.delete()
        return redirect('school_class-list', scpk=scpk)


class SchoolClassCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_class_create.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request, scpk):
        queryset1 = School.objects.filter(id=scpk)
        serializer= SchoolClassSerializer()
        return Response({'serializer': serializer, 'scpk': queryset1 })

    def post(self, request, scpk):
        queryset1 = School.objects.filter(id=scpk)
        queryset = ScClass.objects.filter(school__id=scpk)
        scClass = ScClass.objects.filter(school__id=scpk)
        serializer = SchoolClassSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': scClass, 'scpk': queryset1})
        serializer.save()
        x = School.objects.get(id=scpk)
        z = ScClass.objects.latest('id')
        x.scClass.add(z)
        return redirect('school_class-list', scpk=scpk)

"""  StudentAPI  """

class StudentList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_list.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk, clpk):
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        queryset = Student.objects.filter( scclass__id=clpk)
        return Response({'students': queryset, 'scpk': queryset1, 'clpk': queryset2 })


class StudentDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_detail.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk, clpk, stpk):
        student = get_object_or_404(Student, pk=stpk)
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        serializer_context = {
            'request': request,
        }
        serializer = StudentSerializer(student, context=serializer_context)
        return Response({'serializer': serializer, 'stpk': student, 'scpk': queryset1, 'clpk': queryset2})

    def post(self, request, scpk, clpk, stpk):
        student = get_object_or_404(Student, pk=stpk)
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        serializer_context = {
            'request': request,
        }
        serializer = StudentSerializer(student, data=request.data, context=serializer_context)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'stpk': student, 'scpk': queryset1, 'clpk': queryset2})
        serializer.save()
        return redirect('student-list', clpk=clpk, scpk=scpk )


class StudentDelete(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_delete.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, scpk, clpk, stpk):
        student = get_object_or_404(Student, pk=stpk)
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        return Response({'stpk': student, 'scpk': queryset1, 'clpk': queryset2})

    def post(self, request, scpk, clpk, stpk):
        student = get_object_or_404(Student, pk=stpk)
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        student.delete()
        return redirect('student-list', clpk=clpk, scpk=scpk)


class StudentCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'student_create.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request, scpk, clpk):
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        serializer= StudentSerializer()
        return Response({'serializer': serializer, 'scpk': queryset1, 'clpk': queryset2 })

    def post(self, request, scpk, clpk):
        queryset1 = School.objects.filter(id=scpk)
        queryset2 = ScClass.objects.filter(id=clpk)
        student = ScClass.objects.filter(school__id=scpk)
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            print('in an if statement')
            return Response({'serializer': serializer, 'student': student, 'scpk': queryset1, 'clpk': queryset2})
        serializer.save()
        x = ScClass.objects.get(id=clpk)
        z = Student.objects.latest('id')
        x.student.add(z)
        return redirect('student-list', scpk=scpk, clpk= clpk)

"""User"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
