from django.urls import path
from .views import cards_of_a_deck_view, deck_add_form_view, deck_add_view, deck_delete_view, DeckListView, DeckDetailView , CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView

urlpatterns = [
    path('', DeckListView.as_view(), name='home'),
    #------------------- htmx post request ------------------------------------
    path('decks/<int:deck_id>/', cards_of_a_deck_view, name='deck_detail'), 
    path('deck_form/', deck_add_form_view, name='deck_add_form' ),
    path('deck_add/', deck_add_view, name='deck_add' ),
    path("decks/<int:deck_id>/delete/", deck_delete_view, name="deck_delete"),

    path('add/', CardCreateView.as_view(), name='add_card'),
    path('<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('<int:pk>/delete/', CardDeleteView.as_view(), name='delete_card'),
    path('<int:pk>/edit/', CardUpdateView.as_view(), name='edit_card'),

]
