from django.conf.urls import url

from . import views

app_name = 'objects'
urlpatterns = [
    url(r'^$', views.ObjectsView.as_view(), name='objects'),
]