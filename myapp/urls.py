from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index  , name='index'),
    url(r'submit', views.submit  , name='submit'),
    url(r'sbvr', views.sbvr  , name='sbvr'),
    url(r'ocl', views.ocl  , name='ocl'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)