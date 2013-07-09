from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('zinnia.urls')),
                       url(r'^aktualnosci/',include('zinnia.urls')),
                       url(r'^offers/',include('offers.urls')),
                       url(r'^apartaments/', include('apartaments.urls', namespace="apartaments")),
                       url(r'^reservation/', include('reservation.urls', namespace="reservation")),
                       url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
