from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^', include('{{ project_name }}.core.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
