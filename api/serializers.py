from django.conf import settings
from rest_framework import serializers


class PaySerializer(serializers.Serializer):
    eur_inserted = serializers.DecimalField(decimal_places=2, max_digits=12, required=True, min_value=0.01)

    def validate_eur_inserted(self, eur_inserted):
        return float(eur_inserted)

    def validate(self, attrs):
        if settings.CURRYWURST_PRICE > attrs['eur_inserted']:
            raise serializers.ValidationError('NotEnoughAmountException')
        return attrs
