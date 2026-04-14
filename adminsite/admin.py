from django.contrib import admin
from .models import Course, Instructor, Lesson


# Inline for adding Lessons inside Course
class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Course Admin
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]


# Instructor Admin
class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']


# Register models (ONLY once)
admin.site.register( CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)