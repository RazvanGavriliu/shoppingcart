from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

# urlpatterns = [
#     url(r'', views.product_list, name='product_list'),
#     url(r'^(?P<categoryid>\d+)/$', views.product_list, name='product_list_by_category'),
#     url(r'^(?P<id>\d+)/$', views.product_detail, name='product_detail'),
# ]