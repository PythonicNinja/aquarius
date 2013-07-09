from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext_lazy as _

class Promotion(models.Model):
    topTitle = models.CharField(max_length=255)
    mainTitle = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    image = models.ImageField(_('Teaser Picture'),
                                      upload_to='promotions')
    def __unicode__(self):
        return self.mainTitle

    class Meta:
        verbose_name_plural = 'promotions'


class PromotionPlugin(CMSPlugin):
    topTitle = models.CharField(max_length=255)
    mainTitle = models.CharField(max_length=255)
    content = models.CharField(max_length=255)

    image = models.ImageField(_('Teaser Picture'),
                                      upload_to='promotions')
    def __unicode__(self):
        return self.mainTitle

    class Meta:
        verbose_name_plural = 'promotions'