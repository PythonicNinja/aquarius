from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from .models import Offer, Offers


class Offer(SortableTabularInline):
    fields = ('title', 'price', 'imageField', 'text', 'published')
    model = Offer
    extra = 1

class OffersAdmin(SortableAdmin):
    list_display = ('title','text')
    inlines = (Offer,)

admin.site.register(Offers, OffersAdmin)
