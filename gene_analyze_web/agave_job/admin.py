from django.contrib import admin

from models import Submission

# Register your models here.
class SubmissionAdmin(admin.ModelAdmin):
    pass

# Register new models
admin.site.register(Submission, SubmissionAdmin)