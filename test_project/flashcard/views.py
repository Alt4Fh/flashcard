import json, struct
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator
# Create your views here.
from .models import Card, Deck

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
        return render(request, 'flashcard/includes/deck-item.html', {'deck': deck})
    
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

    


class CardDeleteView(DeleteView):
    model = Card
    # template_name = "flashcard/partials/card_confirm_delete.html"
    success_url = reverse_lazy('home')

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.delete()
    #     return 


def card_delete_confirm_view(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'flashcard/partials/delete_confirm_model.html', {'card': card})



class CardCreateView(CreateView):
    model = Card
    template_name = 'flashcard/card_form.html'
    fields = ['question', 'answer']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "create"
        return context
    
    
class CardUpdateView(UpdateView):
    model = Card    # Specify the model to use
    template_name = 'flashcard/card_form.html'  # Specify the template to use
    fields = ['question', 'answer']  # Specify the fields to include in the form
    
    def form_valid(self, form):
        # Save the updated object
        self.object = form.save()
        # Return an HttpResponse (e.g., JSON response)
        return HttpResponseRedirect(reverse_lazy('card-item',  args=[self.object.id]))

    def form_invalid(self, form):
        # Return an HttpResponse with errors
        return HttpResponse('<h2>No updated</h2>')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "update" 
        return context
    
