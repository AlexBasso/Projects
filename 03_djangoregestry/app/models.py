from django.db import models

class Student(models.Model):
    studentName = models.CharField(max_length=200)
    studentGrade = models.CharField(max_length=200)

    def __str__(self):
        return self.studentName


class ScClass(models.Model):
    scClassName = models.CharField(max_length=200)
    student = models.ManyToManyField(Student)
    professorName = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.scClassName


class School(models.Model):
    schoolName = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey('auth.User', related_name='schools', on_delete=models.CASCADE, blank=True, null=True)
    scClass = models.ManyToManyField(ScClass)

    def __str__(self):
        return self.schoolName

