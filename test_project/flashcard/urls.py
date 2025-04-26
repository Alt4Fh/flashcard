from django.urls import path
from .views import (
    DeckCardView,
    DeckListView,
    DeckDetailView,
    DeckCreateView,
    DeckUpdateView,
    DeckDeleteView,
    CardCreateView,
    CardUpdateView,
    CardDeleteView,

    card_delete_confirm_view,
   
) 

urlpatterns = [
    path('', DeckListView.as_view(), name='home'),
    ## ------ deck --------
    path("deck/create/", DeckCreateView.as_view(), name="deck-create"),
    path("deck/<int:deck_id>/update/", DeckUpdateView.as_view(), name="deck-update"),
    path("deck/<int:pk>/delete/", DeckDeleteView.as_view(), name="deck-delete"), # delete deck confirm view modal on get request and on delete request it will be deleted 
    #---- cards-------------------
    path('cards/', DeckListView.as_view(),  name='card-items'), ## view all card -- home
    #------------------- htmx post request ------------------------------------

    path('decks/<int:pk>/', DeckDetailView.as_view(),  name='deck-item'), ## view deck shows name and no of cards and also return + button for deck
    path('decks/<int:deck_id>/cards/', DeckCardView.as_view(),  name='deck-detail'), ## view cards of a deck
    path('decks/<int:deck_id>/<int:card_id>/', DeckCardView.as_view(),  name='deck-card-item'), ## view a card of a deck
    path('cards/<int:deck_id>/<int:card_id>/', DeckCardView.as_view(), name='card-item'), ## view a card from all a deck
    path("card/<int:deck_id>/create", CardCreateView.as_view(), name="card-create"), ## card creation default deck is id 1
    path("card/<int:card_id>/update", CardUpdateView.as_view(), name="card-update"), # update card  
    path("card/<int:pk>/delete", CardDeleteView.as_view(), name="card-delete"), # delete card confirm view modal on get request and on delete request it will be deleted 


]
