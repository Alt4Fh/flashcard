from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Card

def index(request):
    cards =   Card.objects.all()
    context = {'cards': cards}
    return render(request, 'flashcard/index.html', context)

def add(request):
    return render(request, 'flashcard/add.html')

def edit(request):
    return render(request, 'flashcard/edit.html')

def delete(request):
    return render(request, 'flashcard/delete.html')

def detail(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    context = {'card': card}
    return render(request, 'flashcard/detail.html', context)