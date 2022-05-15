from django.conf import settings
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from api.events import payment_event_processed
from api.models import PayEvent
from api.serializers import PaySerializer
from api.usecases import return_coins


class PayAPIView(CreateAPIView):
    serializer_class = PaySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        coins_returned = return_coins(settings.CURRYWURST_PRICE, serializer.validated_data['eur_inserted'])
        payment_event_processed(serializer.validated_data['eur_inserted'], coins_returned)

        return Response({'data': coins_returned}, status=status.HTTP_201_CREATED)
