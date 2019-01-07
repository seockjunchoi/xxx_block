from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^forgot_passwd/$', views.forgot_passwd, name='forgot_passwd'),
    url(r'^profile/$', views.profile, name='profile'),
]