
from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #
    # Index
    #
    url('^$',
        views.main.index,
        name='index'),
    url('^$',
        views.main.results,
        name='main.results'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)