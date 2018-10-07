from django.conf.urls import url,include
import app.home.views

urlpatterns = [
    url(r'^$', app.home.views.index, name='index'),
    url(r'^index/$', app.home.views.index, name='index'),
]