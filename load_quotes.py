from rest_framework import viewsets
from quotes.models import StoicismQuote
from quotes.serializers import StoicismQuoteSerializer
from django.db.models import F
import random
from rest_framework.response import Response

class StoicismQuoteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = StoicismQuote.objects.all()
    serializer_class = StoicismQuoteSerializer

    def retrieve(self, request, *args, **kwargs):
        # Get a random Stoicism quote
        random_quote = StoicismQuote.objects.order_by('?').first()
        serializer = self.get_serializer(random_quote)
        return Response(serializer.data)
