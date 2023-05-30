from rest_framework import serializers
from .models import School, ScClass, Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    schools = serializers.PrimaryKeyRelatedField(many=True, queryset=School.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'schools']


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = School
        fields =  ('owner', 'id', 'schoolName')


class SchoolClassSerializer(serializers.HyperlinkedModelSerializer):
    school = SchoolSerializer(many=True, read_only=True)

    class Meta:
        model = ScClass
        fields =  ('id', 'scClassName', 'professorName', 'school')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    scClass = SchoolSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields =  ('id', 'studentName', 'studentGrade', 'scClass')
