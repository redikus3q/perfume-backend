from django.urls import path
from . import views

urlpatterns = [
    path('parfume/', views.handle_parfumes, name='handle_parfumes'),
    path('parfume/<id>', views.handle_parfume, name='handle_parfume'),
    path('comments/', views.handle_comments, name='handle_comments'),
    path('comments/parfume/<id>', views.handle_parfume_comments, name='handle_parfume_comments'),
    path('comments/<id>', views.handle_comment, name='handle_comment'),
]