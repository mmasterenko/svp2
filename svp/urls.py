from django.conf.urls import include, url
from django.contrib import admin
from pages import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main, name='main')
]
