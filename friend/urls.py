from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^accept/(?P<user_id>[\w]+)/$', views.accept_request),
	url(r'^reject/(?P<user_id>[\w]+)/$', views.reject_request),
	url(r'^request/(?P<user_id>[\w]+)/$', views.add_user),
	url(r'^(?P<user_id>[\w]+)/$', views.other_user),
]