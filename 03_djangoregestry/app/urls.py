from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path(r'', views.SchoolList.as_view(), name='tmp_school-list'),
    path(r'tmp_school_list/', views.SchoolList.as_view(), name='tmp_school-list'),
    path(r'tmp_school_create/', views.SchoolCreate.as_view(), name='tmp_school-create'),
    path(r'tmp_school_detail/<int:pk>/', views.SchoolDetail.as_view(), name='tmp_school-detail'),
    path(r'tmp_school-list/<int:scpk>/tmp_school_delete/', views.SchoolDelete.as_view(),
         name='tmp_school-delete'),
    path(r'tmp_school-list/<int:scpk>/school_class-list/', views.SchoolClassList.as_view(), name='school_class-list'),
    path(r'tmp_school-list/<int:scpk>/school_class_create/', views.SchoolClassCreate.as_view(), name='school_class-create'),
    path(r'tmp_school_list/<int:scpk>/school_class-list/<int:clpk>/school_class-detail/', views.SchoolClassDetail.as_view(), name='school_class-detail'),
    path(r'tmp_school_list/<int:scpk>/school_class-list/<int:clpk>/school_class_delete/', views.SchoolClassDelete.as_view(),
         name='school_class-delete'),
    path(r'tmp_school_list/<int:scpk>/school_class-list/<int:clpk>/student_list/', views.StudentList.as_view(),
         name='student-list'),
    path(r'tmp_school_list/<int:scpk>/school_class-list/<int:clpk>/student_create/', views.StudentCreate.as_view(),
         name='student-create'),
    path(r'tmp_school_list/<int:scpk>/school_class-list/<int:clpk>/student_list/<int:stpk>/student_detail/',
         views.StudentDetail.as_view(), name='student-detail'),
    path(r'tmp_school_list/<int:scpk>/school_class-list/<int:clpk>/student_list/<int:stpk>/student_delete/',
         views.StudentDelete.as_view(), name='student-delete'),
   ]
