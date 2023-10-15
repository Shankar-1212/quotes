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
class StoicismQuoteCreateView(APIView):
    def post(self, request, format=None):
        author = request.data.get("author")
        text = request.data.get("text")

        if not author or not text:
            return Response({"error": "Both 'author' and 'text' fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        stoicism_quote = StoicismQuote(author=author, text=text)
        stoicism_quote.save()

        serializer = StoicismQuoteSerializer(stoicism_quote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
