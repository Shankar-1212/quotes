from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StoicismQuote
from .serializers import StoicismQuoteSerializer
import random

class RandomStoicismQuote(APIView):
    def get(self, request, format=None):
        try:
            # Get a random Stoicism quote
            random_quote = StoicismQuote.objects.order_by('?').first()
            serializer = StoicismQuoteSerializer(random_quote)
            return Response(serializer.data)
        except StoicismQuote.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
