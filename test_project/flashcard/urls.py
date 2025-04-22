from django.urls import path
from .views import (
    cards_of_a_deck_view, 
    deck_add_form_view, 
    deck_add_view, 
    deck_delete_view, 
    DeckListView,
    CardDeleteView,
    CardUpdateView,
    card_delete_confirm_view,
   
) 

urlpatterns = [
    path('', DeckListView.as_view(), name='home'),
    #------------------- htmx post request ------------------------------------
    path('decks/<int:deck_id>/', cards_of_a_deck_view, name='deck_detail'), 
    path('deck_form/', deck_add_form_view, name='deck_add_form' ),
    path('deck_add/', deck_add_view, name='deck_add' ),
    path("decks/<int:deck_id>/delete/", deck_delete_view, name="deck_delete"),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
    path("card/<int:pk>/update/", CardUpdateView.as_view(), name="card_update"),
    path('card/<int:card_id>/delete_confirm/', card_delete_confirm_view, name="delete_confirm"),
    

   
    
  

]
