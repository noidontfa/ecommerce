from django.urls import path
from .views import index
from django.conf import settings
from django.conf.urls.static import static
app_name = 'core'


urlpatterns = [
    path('',index)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)