# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.payment.views',
     url(r'^$', 'payment', name='payment'),
     url(r'^payment_info/$', 'payment_info', name='payment_info'),
     url(r'^refund/(?P<payment_relation_id>\d+)$', 'payment_refund', name='payment_refund'),
     url(r'^saldo_info/$', 'saldo_info', name='saldo_info'),
     url(r'^saldo/$', 'saldo', name='saldo'),
)