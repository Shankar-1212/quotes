from rest_framework import serializers
from .models import StoicismQuote

class StoicismQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoicismQuote
        fields = '__all__'
