from datetime import timedelta
from email import message
from django.utils import timezone
from django.db import models

class Subject(models.Model):
    subj_name = models.CharField(max_length=200)

    def __str__(self):
        return self.subj_name

class Feedback(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    date_and_time = models.DateTimeField(default=timezone.now())
    modificated = models.BooleanField(default=False, blank=True)

    def was_published_recently(self):
        return self.date_and_time >= timezone.now() - timedelta(days=3)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()

    def __str__(self):
            return '{} - {}'.format(self.name, self.pk)