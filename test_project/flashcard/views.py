import json, struct
from typing import Any
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.
from .models import Card, Deck
from .forms import CardForm

class DeckCardView(View):
    def get(self, request, deck_id=None, card_id=None):
        message = ''
        deck = None
        cards = None
        current_card = None
        current_page = None

        if deck_id:
            # Attempt to retrieve the deck
            try:
                deck = Deck.objects.get(id=deck_id)
                cards = deck.cards.all()
            except Deck.DoesNotExist:
                message = 'No deck found'
            


            if deck and card_id:
                try:
                    current_card = deck.cards.get(id=card_id)
                except Card.DoesNotExist:
                    message = 'The card is not found'
            elif deck:
                current_card = deck.cards.first()

        else:
            # Handle case when no deck_id is provided
            # cards = Card.objects.all()
            if card_id:
                try:
                    current_card = Card.objects.get(id=card_id)
                    #check if ita has deck 
                    if current_card.deck:
                        cards = Deck.objects.get(current_card.deck.id)
                    else: 
                        cards = Card.objects.all()

                except Card.DoesNotExist:
                    message = 'The card is not found'
            else:
                cards = Card.objects.all()
                current_card = cards.first()

        # Fallback message if no cards are found
        if cards:
            # Apply pagination for cards (1 card per page)
            paginator = Paginator(cards, 1)  # 1 card per page
            page_number = request.GET.get('page', 1)  # Get page number from URL query parameter
            try:
                current_page = paginator.page(page_number)
                current_card = current_page.object_list[0]
            except Exception:
                message = 'No cards found for this page'

        
        else:
            message = 'No cards found'

        return render(
            request,
            'flashcard/partials/card-item.html',
            {
                'deck': deck,
                'cards': cards,
                'current_card': current_card,
                'current_page': current_page,
                'message': message,
            }
        )
        



# def cards_of_a_deck_view(request, deck_id):
#     deck = get_object_or_404(Deck, pk=deck_id)
#     cards = deck.cards.all()
#     paginator = Paginator(cards, 1)  # Show 1 card per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     # print(page_obj.object_list[0].question)
#     return render(request, 'flashcard/partials/deck_detail.html', {'deck': deck, 'page_obj': page_obj})


# def deck_add_form_view(request):
#     if request.method == 'POST':
#         deck_id = request.POST.get('deck_id')
#         deck = get_object_or_404(Deck, pk=deck_id)
#         context = {'deck': deck}
#         return render(request, 'flashcard/partials/deck_form.html', context=context)

#     return render(request, 'flashcard/partials/deck_form.html')

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
        return render(request, 'flashcard/includes/deck-item.html', {'deck': deck})
    
    # create new deck
    deck = Deck.objects.create(name=name)
    return render(request, 'flashcard/partials/deck-add-button-item.html', {'deck': deck})



class DeckCreateView(CreateView):
    model = Deck
    fields = '__all__'
    template_name = "flashcard/partials/deck-form.html"
    # success_url
   
    

class DeckUpdateView(UpdateView):
    model = Deck
    template_name = "deck-form.html"


class DeckDeleteView(DeleteView):
    model = Deck
    template_name = "flashcard/partials/delete-confirm-modal.html"

    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        deck_id = self.object.id
        self.object.delete()
        return HttpResponse(f'<div>Deleted Successfull Deck: {deck_id} </div>')

class DeckDetailView(DetailView):
    model = Deck
    template_name = "flashcard/partials/deck-add-button-item.html"



# def deck_delete_view(request, deck_id):
#     deck = get_object_or_404(Deck, pk=deck_id)
#     deck.delete()
#     return HttpResponse('')






class DeckListView(ListView):
    model = Deck
    template_name = 'flashcard/index.html'
    context_object_name = 'decks'

    


class CardCreateView(CreateView):
    form = CardForm
    template_name = 'flashcard/card_form.html'
    fields = ['question', 'answer']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "create"
        return context
    

class CardDeleteView(DeleteView):
    model = Card
    template_name = 'flashcards/partials/delet_confirm_model.html'

   

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        deck = self.object.deck
        self.object.delete()
        # Return to deck after deletion of the card
        return HttpResponseRedirect(reverse_lazy('deck-item', args=[deck.id] ))



def card_delete_confirm_view(request, card_id):
    """
    view to make confirmation on deletion of the card

    """
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'flashcard/partials/delete-confirm-modal.html', {'card': card})


    
class CardUpdateView(UpdateView):
    form = CardForm    # Specify the form
    template_name = 'flashcard/card_form.html'  # Specify the template to use
    
    def form_valid(self, form):
        # Save the updated object
        self.object = form.save()
        # Return the card after the updation
        return HttpResponseRedirect(reverse_lazy('card-item',  args=[self.object.id]))

    def form_invalid(self, form):
        # Return an HttpResponse with errors
        return HttpResponse('<h2>No updated</h2>')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "update" 
        return context
    
