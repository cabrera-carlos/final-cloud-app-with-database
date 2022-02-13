from pyexpat import model
from statistics import mode
from django.contrib import admin
from matplotlib.pyplot import cla
# <HINT> Import any new Models here
from .models import Choice, Course, Lesson, Instructor, Learner, Question

# <HINT> Register QuestionInline and ChoiceInline classes here


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

class QuestionInLine(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 5

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline, QuestionInLine]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)