from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^view/$', views.view, name='view'),
    url(r'^amount/$', views.amount, name='amount'),
    url(r'^charge_money/$', views.charge_money, name='charge_money'),
    url(r'^send_trade_list/$', views.send_trade_list, name='send_trade_list'),
    url(r'^receive_trade_list/$', views.receive_trade_list, name='receive_trade_list'),
    url(r'^send_info/$', views.send_info, name='send_info'),
    url(r'^send_money/$', views.send_money, name='send_money'),
    url(r'^trade_view/$', views.trade_view, name='trade_view'),
    url(r'^cancel_info/$', views.cancel_info, name='cancel_info'),
    #url(r'^test_reg/$', views.test_reg, name='test_reg'),
    #url(r'^amount/$', views.forgot_passwd, name='forgot_passwd'),
    #url(r'^trade__list/$', views.profile, name='profile'),
]