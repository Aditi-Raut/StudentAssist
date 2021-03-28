from urllib import request

from django.shortcuts import render, get_object_or_404, redirect
from teacher.models import *


def home(request):
    user = request.user
    if user.is_anonymous:
        return redirect('/signup')

    enrolled = Attendee.objects.filter(student=user)

    return render(request, 'dashboard.html', context={'enrolled': enrolled})


def viewcourses(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)

    lectures = Lecture.objects.filter(course=course)
    if (request.method == 'GET'):
        return render(request, 'coursedetails.html', {'course': course, 'lectures': lectures})


def course(request):
    return render(request, 'course.html')


def streamcourse(request, lecture_pk):
    lecture = get_object_or_404(Lecture, pk=lecture_pk)
    links = Links.objects.filter(lecture=lecture)
    if (request.method == 'GET'):
        return render(request, 'course_stream.html', {'lecture': lecture, 'links':links})
    else:
        comment = Comment(post=lecture,student=request.user,text=request.POST.get('question'))
        comment.save()
        return redirect(streamcourse, lecture_pk)
