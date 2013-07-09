from django.template.response import TemplateResponse
from .models import Offer, Offers
__author__ = 'wojtek'

def offers_list(request):
    #pobac z modeli elementy
    offers = Offers.objects.all()
    offer = Offer.objects.all().filter(offers = offers, published=True)
    context = {'offers': offers,
               'offer': offer}
    return TemplateResponse(request, 'offers.html', context=context)
