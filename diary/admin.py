from django.contrib import admin

from diary.models import Owner, DiaryEntries, Feedback
admin.site.register([Owner,Feedback, DiaryEntries])
