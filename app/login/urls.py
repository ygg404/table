from django.conf.urls import url,include
import app.login.views

urlpatterns = [
    url(r'^$', app.login.views.index,name='index' ),
    url(r'^index$', app.login.views.index,name='index' ),
    url(r'^CheckLogin$', app.login.views.CheckLogin,name='CheckLogin' ),
]