__author__ = 'Emanuele Palazzetti <emanuele.palazzetti@gmail.com>'

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __unicode__(self):
        return self.name


class Course(models.Model):
    COURSE_TYPE_CHOICES = (
        (0, 'Full course'),
        (1, 'Laboratory'),
    )

    name = models.CharField(max_length=200, null=False)
    type = models.IntegerField(choices=COURSE_TYPE_CHOICES, default=0)
    credits = models.IntegerField(default=0)
    department = models.ForeignKey(Department, related_name="courses")

    def __unicode__(self):
        return u"{} ({} cfu)".format(self.name, self.credits)


class Exam(models.Model):
    HONORS_CHOICES = (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )

    course = models.ForeignKey(Course)
    registration_date = models.DateField('Registration date', null=False, default=datetime.now())
    vote = models.IntegerField(default=0)
    honors = models.CharField(max_length=3, default='No', choices=HONORS_CHOICES)
    note = models.CharField(max_length=200, null=True)

    def __unicode__(self):
        return u"{} - {} (honors: {})".format(self.course, self.vote, self.honors)
