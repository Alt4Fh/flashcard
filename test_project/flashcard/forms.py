from django import forms
from .models import Deck, Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['deck', 'question', 'answer']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deck'].queryset = Deck.objects.all()
        self.fields['deck'].widget.attrs.update({'size' : 10})

