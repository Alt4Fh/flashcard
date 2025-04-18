import json, struct
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Card, Deck


def cards_of_a_deck_view(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    cards = deck.cards.all()
    return render(request, 'flashcard/deck_detail.html', {'deck': deck, 'cards': cards})


def deck_add_form_view(request):
    if request.method == 'POST':
        deck_id = request.POST.get('deck_id')
        deck = get_object_or_404(Deck, pk=deck_id)
        context = {'deck': deck}
        return render(request, 'flashcard/partials/deck_form.html', context=context)

    return render(request, 'flashcard/partials/deck_form.html')

@require_POST
def deck_add_view(request):
    name = request.POST.get('name')
    deck_id = request.POST.get('deck_id')
    print(deck_id)
    if deck_id: 
    # update deck name    
        deck = get_object_or_404(Deck, pk=deck_id)
        deck.name = name
        deck.save()
        return render(request, 'flashcard/includes/deck_item.html', {'deck': deck})
    
    # create new deck
    deck = Deck.objects.create(name=name)
    return render(request, 'flashcard/partials/deck_add_button_item.html', {'deck': deck})


def deck_delete_view(request, deck_id):
    deck = get_object_or_404(Deck, pk=deck_id)
    deck.delete()
    return HttpResponse('')

class DeckListView(ListView):
    model = Deck
    template_name = 'flashcard/index.html'
    context_object_name = 'decks'




class DeckDetailView(DetailView):
    model = Deck
    template_name = 'flashcard/deck_detail.html'
    context_object_name = 'deck'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        return render(request, self.template_name, self.get_context_data(object=self.object))


class CardListView(ListView):
    model = Card
    template_name = 'flashcard/card_list.html'
    context_object_name = 'cards'

class CardDetailView(DetailView):
    model = Card
    template_name = 'flashcard/card_detail.html'
    context_object_name = 'card'

class CardDeleteView(DeleteView):
    model = Card
    template_name = "flashcard/card_confirm_delete.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return 


class CardCreateView(CreateView):
    model = Card
    template_name = 'flashcard/card_form.html'
    fields = ['question', 'answer']
    success_url = reverse_lazy('card_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "create"
        return context
    
    
class CardUpdateView(UpdateView):
    model = Card    # Specify the model to use
    template_name = 'flashcard/card_form.html'  # Specify the template to use
    fields = ['question', 'answer']  # Specify the fields to include in the form
    success_url = reverse_lazy('card_list')  # Specify the URL to redirect to after successful form submission  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "update" 
        return context
    
