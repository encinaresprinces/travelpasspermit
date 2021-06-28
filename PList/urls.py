from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from PList import views


urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	

	url(r'^new$', views.new_item, name='new_item'),
    url(r'^(\d+)/view_list$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
	url(r'^signup2$', views.signup2, name='signup2'),
	url(r'^signup3$', views.signup3, name='signup3'),
	url(r'^signup4$', views.signup4, name='signup4'),

    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
    ]

	



'''url(r'Login/', views.login, name='login'),
	url(r'Sgnup/', views.sgnup, name='sgnup'),
	url(r'Signup//', views.signup, name='signup'),
	url(r'ssup/', views.ssup, name='ssup'),
	url(r'ssupp/', views.ssupp, name='ssupp'),'''







'''urlpatterns = [
	path('', views.home_page),
	path('Login.html', views.login, name='Login'),
	path('Sgnup.html', views.signup1, name='Sgnup'),
	path('Signup.html', views.signup2, name='Signup'),
	path('ssup.html', views.signup3, name='ssup'),
	path('ssupp.html', views.signup4, name='ssupp'),
]'''