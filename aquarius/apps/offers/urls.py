from django.conf.urls.defaults import *

urlpatterns = patterns('offers.views',
    url(r'^$', 'offers_list', name='offers_list'),
)

