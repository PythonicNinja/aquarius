# -*- coding: utf-8 -*-
import datetime
from apartaments.models import Apartament

from reservation.forms import ContactForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from reservation.models import CalendarDay


def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request, request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            obj = form.save()
            # Process the data in form.cleaned_data
            send_mail(u'Zapytanie ze strony willa-magnolia.pl', u'Osoba kontaktowa: %s,\nRezerwacja od: %s,\nRezerwacja do: %s,\nAdres e-mail: %s,\nTel.: %s' % (obj.last_name, obj.start_date, obj.end_date, obj.client_email_address, obj.phone ), 'Willa Magnolia Gdynia <willa@gdynia-magnolia.pl>', ['willa@gdynia-magnolia.pl'])
            if obj.client_email_address:
                send_mail(u'Wiadomość ze strony gdynia-magnolia.pl potwierdzenie rezerwacji', u'Dziękujemy za rezerwację. Odpowiemy tak szybko jak to możliwe.\nWilla\nMagnolia\nGdynia\n', 'Willa Magnolia <willa@gdynia-magnolia.pl>', [obj.client_email_address])
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    elif request.method == 'GET':
        # form = ContactForm(self.fields['start_date']=request.GET)
        form = ContactForm(request = request)
        context = {
               'form': form,
               }
        return render(request, 'reservation/contact.html', context)


def month_calendar(request, year, month, slug):
    try:
        month = datetime.date(year=int(year), month=int(month), day=1)
    except ValueError:
        raise Http404
    print slug
    get_object_or_404(Apartament,slug=slug)
    return HttpResponse(
        CalendarDay.objects.get_html_calendar(month.year, month.month, slug))