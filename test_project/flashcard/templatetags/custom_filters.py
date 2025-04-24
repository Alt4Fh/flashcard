from django import template
from flashcard.models import Card

# register = template.Library()

# @register.filter
# def get_next_index(cards, id):
#     try:
#         cards_touple = zip(range(len(cards)), cards)
#         return value[index]
#     except IndexError:
#         return None


# @register.filter
# def get_prev_index(value, index):
#     try:
#         return value[index]
#     except IndexError:
#         return None