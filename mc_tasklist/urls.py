from django.urls import path

from . import views


app_name = 'mc_tasklist'
urlpatterns = [
    path('', views.hello, name='index'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('motivation/', views.motivation, name='motivation'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('list-subject/', views.list_subject, name='list_subject'),
    path('edit-subject/<int:sub_id>/', views.edit_subject, name='edit_subject'),
    path('delete-subject/<int:sub_id>/', views.delete_subject, name='delete_subject'),
    path('confirm-delete-subject/<int:sub_id>/', views.confirm_delete_subject, name='confirm_delete_subject'),
    path('feedback-detail/<int:feedback_id>/', views.feedback_detail, name='feedback_detail'),
    path('edit-feedback-detail/<int:feedback_id>/', views.edit_feedback_post, name='edit_feedback_detail'),
    path('confirm-delete-feedback/<int:feedback_id>/', views.confirm_delete_feedback, name='confirm_delete_feedback'),
    path('delete-feedback/<int:feedback_id>/', views.delete_feedback_post, name='delete_feedback'),
]