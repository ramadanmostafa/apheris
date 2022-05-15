from django.conf import settings


def return_coins(currywurst_price: float, eur_inserted: float) -> dict:
    result = {}
    if currywurst_price == eur_inserted:
        return result
    reminder = eur_inserted - currywurst_price
    for coin in settings.COINS:
        if reminder <= 0:
            break
        if reminder >= coin:
            result[coin] = reminder // coin
            reminder = round(reminder % coin, 2)
    return result
