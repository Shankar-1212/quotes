from django.urls import path
from quotes.views import RandomStoicismQuote, StoicismQuoteCreateView
urlpatterns = [
    path('', RandomStoicismQuote.as_view(), name='random_stoicism_quote'),
    path('quotes/create/', StoicismQuoteCreateView.as_view(), name='create-stoicism-quote'),
]
