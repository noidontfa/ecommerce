from django.urls import path
from .views import HomePage, ProductDetail, index
from django.conf import settings
from django.conf.urls.static import static
app_name = 'core'


urlpatterns = [
    path('',HomePage.as_view(),name='home-page'),
    path('detail/<slug>',ProductDetail.as_view(),name='product-detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)