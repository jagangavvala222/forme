from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from testapp import views


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^admin/comdb/dnintr/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
