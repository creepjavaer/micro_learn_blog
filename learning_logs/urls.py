# define the url of the learning_logs 

from django.conf.urls import url
from . import views

urlpatterns=[url(r'^$',views.index,name='index'),]