from django.conf import settings


def shop_info(request):

    count = 0
    try:
        if request.session['bucket']:
            count = 0
    except KeyError:
        request.session['bucket'] = []
        request.session['validated'] = False
    

    return {
        'shop_count': count
    }

def get_contact(request):

    return {
        'confo_telephone': "+213 551 46 20 06",
        'confo_address': "02 Cité Tchilel, Alger"
    }