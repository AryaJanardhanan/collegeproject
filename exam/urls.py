from django.urls import re_path,include
from django.contrib import admin
from exam import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import re_path
urlpatterns = [
   
   
    


    re_path(r'^$',views.home_view,name=''),
    re_path(r'^logout$', LogoutView.as_view(template_name='exam/logout.html'),name='logout'),
    re_path(r'^afterlogin$', views.afterlogin_view,name='afterlogin'),



    re_path(r'^adminclick$', views.adminclick_view),
    re_path(r'^adminlogin$', LoginView.as_view(template_name='exam/adminlogin.html'),name='adminlogin'),
    re_path(r'^admin-dashboard$', views.admin_dashboard_view,name='admin-dashboard'),

    re_path(r'^admin-view-marks/<int:pk>$', views.admin_view_marks_view,name='admin-view-marks'),

    re_path(r'^admin-course$', views.admin_course_view,name='admin-course'),
    re_path(r'^admin-add-course$', views.admin_add_course_view,name='admin-add-course'),
    re_path(r'^admin-view-course$', views.admin_view_course_view,name='admin-view-course'),
    re_path(r'^delete-course/<int:pk>$', views.delete_course_view,name='delete-course'),

    re_path(r'^admin-question$', views.admin_question_view,name='admin-question'),
    re_path(r'^admin-add-question$', views.admin_add_question_view,name='admin-add-question'),
    re_path(r'^admin-view-question$', views.admin_view_question_view,name='admin-view-question'),
    re_path(r'^view-question/<int:pk>$', views.view_question_view,name='view-question'),
    re_path(r'^delete-question/<int:pk>$', views.delete_question_view,name='delete-question'),


]