from django.urls import path
from .views import (
    deck_add_form_view, 
    deck_add_view, 
    deck_delete_view, 
    DeckCardView,
    DeckListView,
    CardDeleteView,
    CardUpdateView,
    CardCreateView,

    card_delete_confirm_view,
   
) 

urlpatterns = [
    path('', DeckListView.as_view(), name='home'),
    #------------------- htmx post request ------------------------------------

    path('decks/<int:deck_id>/', DeckCardView.as_view(),  name='deck-item'), ## view cards of a deck
    path('decks/<int:deck_id>/<int:card_id>/', DeckCardView.as_view(),  name='deck-card-item'), ## view a card of a deck
    path('cards/', DeckCardView.as_view(),  name='card-items'), ## view all card
    path('cards/<int:card_id>/', DeckCardView.as_view(), name='card-item'), ## view a card from all cards

    path('deck_form/', deck_add_form_view, name='deck_add_form' ),
    path('deck_add/', deck_add_view, name='deck_add' ),
    path("decks/<int:deck_id>/delete/", deck_delete_view, name="deck_delete"),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
    path("card/<int:pk>/update/", CardUpdateView.as_view(), name="card-update"),
    path("card/create/", CardCreateView.as_view(), name="card-create"),
    path('card/<int:card_id>/delete_confirm/', card_delete_confirm_view, name="delete_confirm"),
    

]
