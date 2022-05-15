from django.conf import settings

from api.models import PayEvent


def payment_event_processed(eur_inserted, coins_returned):
    event = PayEvent.objects.create(
        data={
            'CURRYWURST_PRICE': settings.CURRYWURST_PRICE,
            'EUR_INSERTED': eur_inserted,
            'RETURN_COINS': coins_returned,
        }
    )
    event.dispatch()
