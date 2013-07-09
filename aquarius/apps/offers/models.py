from django.db import models
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey
from tinymce.models import HTMLField

class Offers(Sortable):

    title = models.CharField(max_length=255)
    text = HTMLField(_('teaserText'))

    class Meta(Sortable.Meta):
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')

    def __unicode__(self):
        return self.title


class Offer(Sortable):
    offers = SortableForeignKey(Offers, related_name='offers',
                               verbose_name=_('offers'))
    title = models.CharField(max_length=255)

    price = models.CharField(_('Price'),max_length=255, blank=True)

    published = models.BooleanField(_('Published'), default=True)

    imageField = models.ImageField(_('Image'), upload_to='offer',
                                    blank=True)
    text = HTMLField(_('teaserText'))


    class Meta(Sortable.Meta):
        verbose_name = _('offer')
        verbose_name_plural = _('offers')

    def __unicode__(self):
        return self.offers.title
