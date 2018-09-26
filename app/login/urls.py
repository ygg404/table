from django.conf.urls import url,include
import app.login.views

urlpatterns = [
    url(r'^index/$', app.login.views.index,name='index' ),
]