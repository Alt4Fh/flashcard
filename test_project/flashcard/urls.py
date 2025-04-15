from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add_flashcard'),
    path('edit/<int:flashcard_id>/', views.edit, name='edit_flashcard'),
    path('delete/<int:flashcard_id>/', views.delete, name='delete_flashcard'),
    path('detail/<int:card_id>/', views.detail, name='card_detail'),

]
