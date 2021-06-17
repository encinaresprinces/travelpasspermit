from django.conf.urls import url , include
from django.contrib import admin
from django.urls import path
from PList import views


urlpatterns = [
	url(r'^$', views.home_page, name='home_page'),
	url('Login/', views.login, name='login'),
	url('Sgnup/', views.signup1, name='sgnup'),
	url('signup/', views.signup2, name='signup'),
	url('ssup/', views.signup3, name='ssup'),
	url('ssupp/', views.signup4, name='ssupp'),
]




'''urlpatterns = [
	path('', views.home_page),
	path('Login.html', views.login, name='Login'),
	path('Sgnup.html', views.signup1, name='Sgnup'),
	path('Signup.html', views.signup2, name='Signup'),
	path('ssup.html', views.signup3, name='ssup'),
	path('ssupp.html', views.signup4, name='ssupp'),
]'''