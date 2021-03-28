import smtplib

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Course, Lecture, Links, Attendee
from .forms import LectureCreationForm, CourseCreationForm, AttendeeCreationForm
import requests
from bs4 import BeautifulSoup


def home(request):
    user = request.user
    if user.is_anonymous:
        return redirect('/signup')

    teacher = get_object_or_404(Teacher, user=user)
    courses = Course.objects.filter(teacher=teacher)

    return render(request, 'teacher.html', context={'teacher': teacher, 'courses': courses})


def viewcourse(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    lectures = Lecture.objects.filter(course=course)
    if (request.method == 'GET'):
        return render(request, 'coursedetail.html', {'course': course, 'lectures': lectures})


@login_required
def createlec(request, course_pk):
    # print("Hello")
    if (request.method == 'GET'):
        return render(request, 'createlec.html', {'form': LectureCreationForm()})
    else:
        try:
            form = LectureCreationForm(request.POST, request.FILES)
            newlec = form.save(commit=False)
            course = get_object_or_404(Course, pk=course_pk)
            newlec.teacher = course.teacher
            newlec.course = course
            newlec.save()
            return redirect(selectlinks, newlec.id)
        except ValueError:
            return render(request, 'createlec.html', {'form': LectureCreationForm(), 'error': 'Bad Data Passed In. Try Again'})




@login_required
def createcourse(request):
    if (request.method == 'GET'):
        return render(request, 'createcourse.html', {'form': CourseCreationForm()})
    else:
        try:
            # print("Hello")
            form = CourseCreationForm(request.POST, request.FILES)
            newcourse = form.save(commit=False)
            teacher = get_object_or_404(Teacher, user=request.user)
            newcourse.teacher = teacher
            newcourse.save()
            return redirect(home)
        except ValueError:
            return render(request, 'createcourse.html', {'form': CourseCreationForm(), 'error': 'Bad Data Passed In. Try Again'})


def selectlinks(request, lecture_pk):
    lecture = get_object_or_404(Lecture, pk=lecture_pk)
    count = 0
    t1=[]
    t2=[]
    t3=[]
    tg1, tg2, tg3 = lecture.tag1, lecture.tag2, lecture.tag3

    url1 = 'https://google.com/search?q=' + tg1
    reqs1 = requests.get(url1)
    soup1 = BeautifulSoup(reqs1.text, 'html.parser')


    for link in soup1.find_all('a', {"href": True}):
        res = (link.get('href'))
        if (res.startswith("http")):
            count += 1
            t1.append(res)
        if count == 5:
            break
    # print("T1:", t1)
    url2 = 'https://google.com/search?q=' + tg2
    reqs2 = requests.get(url2)
    soup2 = BeautifulSoup(reqs2.text, 'html.parser')
    count=0

    for link in soup2.find_all('a', {"href": True}):
        res2 = (link.get('href'))
        if (res2.startswith("http")):
            count += 1
            t2.append(res2)
        if count == 5:
            break
    # print("T2:", t2)
    url3 = 'https://google.com/search?q=' + tg3
    reqs3 = requests.get(url3)
    soup3 = BeautifulSoup(reqs3.text, 'html.parser')
    count=0

    for link in soup3.find_all('a', {"href": True}):
        res3 = (link.get('href'))
        if (res3.startswith("http")):
            count += 1

            t3.append(res3)
        if count == 5:
            break
    # print("T#:", t3)
    links = t1+t2+t3
    if (request.method == 'GET'):
        return render(request, 'selectlinks.html', {'links': links, 'lecture': lecture})
    else:
        try:
            lecture = get_object_or_404(Lecture, pk=lecture_pk)

            teacher = get_object_or_404(Teacher, user=request.user)
            some_var = request.POST.getlist('checks[]')
            for i in some_var:
                link=Links(teacher=teacher, lecture=lecture, links=i)
                link.save()
            return redirect(viewcourse, lecture.course.id)
        except ValueError:
            return render(request, 'selectlinks.html', {'links': links, 'lecture': lecture, 'error':'please try again'})


@login_required
def createattendee(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    attendees = Attendee.objects.filter(course=course)
    if (request.method == 'GET'):
        return render(request, 'createattendee.html', {'attendees':attendees})
    else:
        try:
            mail = request.POST.get('email')
            teacher = course.teacher
            try:
               user = User.objects.get(email=mail)

               user.is_active=True
               user.save()
               att = Attendee(teacher=teacher, student=user, course=course)
               att.save()
               sendmail(mail)
               return render(request, 'createattendee.html', {'attendees': attendees,'msg': 'Student has been enrolled'})
            except User.DoesNotExist:
                return render(request, 'createattendee.html',{'attendees': attendees, 'msg': 'Student with given email not found'})
        except ValueError:
            return render(request, 'createattendee.html', {'attendees':attendees,'msg': 'Bad Data Passed In. Try Again'})


def sendmail(to):
    content = "Hello, Your Teacher has enrolled you into the course."
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('abc@gmail.com', 'password@123')
    server.sendmail('abc@gmail.com', to, content)
    server.close()
