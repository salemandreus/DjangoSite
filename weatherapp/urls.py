from django.conf.urls import url, include
from django.contrib import admin

from collection import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^days/(?P<slug>[-\w]+)/$', views.day_detail, name='day_detail'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
