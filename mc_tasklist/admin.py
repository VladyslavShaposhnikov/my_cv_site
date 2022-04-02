from django.contrib import admin
from .models import Feedback, Subject, Contact

admin.site.register(Feedback)
admin.site.register(Subject)
admin.site.register(Contact)