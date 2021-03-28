from django.forms import ModelForm
from .models import Attendee, Lecture, Course, Comment


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'image', 'description']


class LectureCreationForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'video', 'note', 'tag1', 'tag2', 'tag3', 'description' ]


class AttendeeCreationForm(ModelForm):
    class Meta:
        model = Attendee
        fields = ['student']


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
