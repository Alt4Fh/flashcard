from django.db import models
from django.urls import reverse

# Create your models here.

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    def __str__(self):
        return self.question
    


class Deck(models.Model):
    name = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)
    def __str__(self):
        return self.name    
    
    