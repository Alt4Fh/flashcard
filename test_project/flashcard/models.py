from django.db import models
from django.urls import reverse_lazy

# Create your models here.



class Deck(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):

        return reverse_lazy("deck-item", kwargs={"deck_id": self.pk})
    

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='cards') ## on deletion of deck every card will be deleted
    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse_lazy("card-item", kwargs={"card_id": self.pk})
    
    