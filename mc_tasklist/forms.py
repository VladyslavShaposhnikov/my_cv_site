from django import forms
from .models import Feedback


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, label='Company name')
    email = forms.EmailField(max_length=200, label='E-mail')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject', 'name', 'email', 'message')
        labels = {
            'name': ('Your name or company name'),
            'subject': ('Issue title'),
            'message': ('Tip for me'),
            'email': ('E-mail'),
        }
        widgets = {
            'email': forms.EmailInput,
        }


class AddSubjectForm(forms.Form):
    create_sub = forms.CharField(max_length=200, label='Issue title')

class EditSubjectForm(forms.Form):
    edit_sub = forms.CharField(max_length=200, label='New issue title')