from django.db import models

# Create your models here.

class Card(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('card_detail', args=[str(self.id)])


class Deck(models.Model):
    name = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)
    def __str__(self):
        return self.name    
    
    