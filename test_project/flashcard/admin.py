from django.contrib import admin

# Register your models here.

from .models import Card, Deck
admin.site.register(Card)


@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    pass
