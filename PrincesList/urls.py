from django.conf.urls import url
from PList import views
#from django.urls import path
#from django.http import HttpResponse

urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^PList/new$', views.new_list, name='new_list'),    
    url(r'^PList/(\d+)/$', views.view_list, name='view_list'),    
    url(r'^PList/(\d+)/add_item$', views.add_item, name='add_item')]