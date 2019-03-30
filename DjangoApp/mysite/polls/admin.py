from django.contrib import admin
from .models import Question


# Register your models here.

"""
Admin Customize 1
=====================

class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
"""

"""
Admin Customize 2 ( fieldsets )
=====================
"""
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               { 'fields' : ['question_text']}),
        ('Date Information', { 'fields' : ['pub_date']}),

    ]

admin.site.register(Question, QuestionAdmin)