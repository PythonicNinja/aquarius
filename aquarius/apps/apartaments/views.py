import datetime
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404

from .models import Apartament, Photos
from reservation.models import CalendarDay

__author__ = 'wojtek'


def apartaments_list(request):
    #pobac z modeli elementy
    apartaments = Apartament.objects.all()
    context = {'apartaments': apartaments}
    return TemplateResponse(request, 'apartaments.html', context=context)


def apartaments_free_list(request):
    start = request.GET.get('arrival')
    end = request.GET.get('comingback')
    persons = request.GET.get('persons')

    aparamentOCCUPIED = CalendarDay.objects.all().filter(date__range=[start, end],state=2)
    apartaments = Apartament.objects.all().filter(maxPeople__gte=persons)

    for occupied in aparamentOCCUPIED:
        apartaments = [apatament for apatament in apartaments if apatament.name != occupied.apartament.name]

    context = {'apartaments': apartaments,
               'start': start,
               'end': end,
               }
    return TemplateResponse(request, 'apartaments.html', context=context)

def apartament_detail(request, slug):
    #pobrac z modeli element na podstawie sluga
    apartament = get_object_or_404(Apartament, slug=slug)

    photos = Photos.objects.filter(apartament=apartament, published=True)
    now = datetime.datetime.now()

    context = {'apartament': apartament,
               'listOfPhotos': photos,
               'calendar': CalendarDay.objects.get_html_calendar(now.year,
                                                                now.month, slug)
    }

    return TemplateResponse(request, 'apartament.html', context=context)
