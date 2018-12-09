from django.conf.urls import url,include
import app.webapi.views

urlpatterns = [
    url(r'^GetUserInfo', app.webapi.views.GetUserInfo,name='GetUserInfo' ),
]