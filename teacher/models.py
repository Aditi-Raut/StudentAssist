from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Teacher(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(User, unique=True, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    qualification = models.CharField(max_length=200, blank=True)

    def _str_(self):
        return self.user


class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='teacher/images', blank=True)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def _str_(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='teacher/videos', null=True, verbose_name="")
    tag1 = models.TextField(max_length=100, blank=True)
    tag2 = models.TextField(max_length=100, blank=True)
    tag3 = models.TextField(max_length=100, blank=True)

    description = models.TextField(blank=True)
    note = models.FileField(upload_to='teacher/notes', null=True, verbose_name="")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.title) + '-' + str(self.course) + '-' + str(self.teacher)


class Links(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    links = models.URLField(max_length=200)


class Attendee(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.course) + '-' + str(self.student)


class Comment(models.Model):
    post = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='comments')
    student = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.text
