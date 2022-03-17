from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ContactForm, FeedbackForm, AddSubjectForm, EditSubjectForm
from .models import Feedback, Subject
from django.core.mail import send_mail
from django.contrib import messages


def hello(request):
    return render(request, 'mc_tasklist/index.html')

def about(request):
    return render(request, 'mc_tasklist/about.html')

def skills(request):
    return render(request, 'mc_tasklist/skills.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            final_message = 'Company: {}\nE-mail: {}\n'.format(name, email) + message
            my_mail = 'shapik2404@gmail.com'
            send_mail(subject=subject, message=final_message, from_email=my_mail, recipient_list=[my_mail])
            messages.add_message(request, messages.SUCCESS, 'Thank you for your message :)')
            return HttpResponseRedirect(reverse('mc_tasklist:contact'))
    else:
        form = ContactForm()
        return render(request, 'mc_tasklist/contact.html', {'form': form})

def feedback(request):
    feedback_list = Feedback.objects.order_by('-date_and_time')
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            subj_name = Subject.objects.get(subj_name=subject)
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            create_feedback = Feedback.objects.create(name=name, email=email, subject=subj_name, message=message)
            create_feedback.save()
            return HttpResponseRedirect(reverse('mc_tasklist:feedback'))
    else:
        form = FeedbackForm()
    return render(request, 'mc_tasklist/feedback.html', {
        'form': form,
        'feedback_list': feedback_list,
    })

def motivation(request):
    return render(request, 'mc_tasklist/motivation.html')

def add_subject(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['create_sub']
            subj_name = Subject.objects.create(subj_name=subject)
            subj_name.save()
            return HttpResponseRedirect(reverse('mc_tasklist:feedback'))
    else: 
        form = AddSubjectForm()
        return render(request, 'mc_tasklist/add_subject.html', {'form': form})

def list_subject(request):
    subjects = Subject.objects.all()
    return render(request, 'mc_tasklist/list_subject.html', {'subjects': subjects})

def edit_subject(request, sub_id):
    title_to_edit = Subject.objects.get(pk=sub_id)
    if request.method == 'POST':
        form = EditSubjectForm(request.POST, initial={'edit_sub': title_to_edit})
        if form.is_valid():
            subject = form.cleaned_data['edit_sub']
            Subject.objects.filter(pk=sub_id).update(subj_name=subject)
            return HttpResponseRedirect(reverse('mc_tasklist:feedback'))
    else: 
        form = EditSubjectForm(initial={'edit_sub': title_to_edit})
        return render(request, 'mc_tasklist/edit_subject.html', {'form': form, 'title_to_edit': title_to_edit})

def delete_subject(request, sub_id):
    Subject.objects.filter(pk=sub_id).delete()
    return HttpResponseRedirect(reverse('mc_tasklist:feedback'))

def confirm_delete_subject(request, sub_id):
    subject = Subject.objects.get(pk=sub_id)
    return render(request, 'mc_tasklist/confirm_delete.html', {'subject': subject})

def feedback_detail(request, feedback_id):
    feedback_post = Feedback.objects.get(pk=feedback_id) 
    return render(request, 'mc_tasklist/feedback_detail.html', {'feedback_post': feedback_post})

def edit_feedback_post(request, feedback_id):
    post_to_edit = Feedback.objects.get(pk=feedback_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, initial={
            'name': post_to_edit.name,
            'subject': post_to_edit.subject,
            'message': post_to_edit.message,
            'email': post_to_edit.email,
        })
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            subj_name = Subject.objects.get(subj_name=subject)
            message_text = form.cleaned_data['message']
            email = form.cleaned_data['email']
            Feedback.objects.filter(pk=feedback_id).update(name=name, email=email, subject=subj_name, message=message_text, date_and_time=timezone.now(), modificated=True)
            return HttpResponseRedirect(reverse('mc_tasklist:feedback'))
    else: 
        form = FeedbackForm(initial={
            'name': post_to_edit.name,
            'subject': post_to_edit.subject,
            'message': post_to_edit.message,
            'email': post_to_edit.email,
        })
    return render(request, 'mc_tasklist/edit_feedback_post.html', {'form': form, 'post_to_edit': post_to_edit})

def delete_feedback_post(request, feedback_id):
    Feedback.objects.filter(pk=feedback_id).delete()
    return HttpResponseRedirect(reverse('mc_tasklist:feedback'))

def confirm_delete_feedback(request, feedback_id):
    feedback = Feedback.objects.get(pk=feedback_id)
    return render(request, 'mc_tasklist/confirm_delete_feedback.html', {'feedback': feedback})