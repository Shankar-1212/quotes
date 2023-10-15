from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StoicismQuote
from .serializers import StoicismQuoteSerializer
from random import randint

class RandomStoicismQuote(APIView):
    def get(self, request, format=None):
        try:
            # Get a random Stoicism quote
            x=randint(0, 10000)
            random_quote = StoicismQuote.objects.all()[x]
            serializer = StoicismQuoteSerializer(random_quote)
            return Response(serializer.data)
        except StoicismQuote.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def perform_create(self, serializer):
        serializer.save(author=self.request.user.username, text=self.request.data['text'])