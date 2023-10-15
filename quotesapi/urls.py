from django.urls import path
from quotes.views import RandomStoicismQuote

urlpatterns = [
    path('', RandomStoicismQuote.as_view(), name='random_stoicism_quote'),
    path('create/', RandomStoicismQuote.as_view(), name='create_stoicism_quote'),
]
