__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from exams import views


urlpatterns = patterns('',
    # APIs urls
    url(r'^department/$', views.DepartmentList.as_view()),
    url(r'^department/(?P<pk>[0-9]+)/$', views.DepartmentDetail.as_view()),
    url(r'^course/$', views.CourseList.as_view()),
    url(r'^course/(?P<pk>[0-9]+)/$', views.CourseDetail.as_view()),
    url(r'^exam/$', views.ExamList.as_view()),
    url(r'^exam/(?P<pk>[0-9]+)/$', views.ExamDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)
