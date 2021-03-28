from django.contrib import admin
from .models import Teacher, Attendee, Course, Lecture, Links, Comment

admin.site.register(Teacher)
admin.site.register(Attendee)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Links)

admin.site.register(Comment)
