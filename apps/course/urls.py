from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'add$', views.add),
    url(r'courses/destroy/(?P<id>\d+)$', views.delete),
    url(r'delete$', views.destroy),
]