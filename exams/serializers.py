__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from rest_framework import serializers
from exams.models import Department, Course, Exam


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course


class ExamSerializer(serializers.ModelSerializer):
    course = serializers.RelatedField(read_only=True)

    class Meta:
        model = Exam
