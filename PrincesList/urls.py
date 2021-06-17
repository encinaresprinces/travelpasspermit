from django.contrib import admin
from django.urls import path, include
#from django.urls import path
#from django.http import HttpResponse


urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('PList.urls')),
]

'''urlpatterns = [    
    url(r'^$', views.home_page, name='home_page'),    
    url(r'^PList/new$', views.new_list, name='new_list'),    
    path('admin/', admin.site.urls),
    path('', include('PList.urls')),
    url(r'^PList/(\d+)/$', views.view_list, name='view_list'),    
    url(r'^PList/(\d+)/add_item$', views.add_item, name='add_item')]'''




