from django.conf.urls import url

from . import views

app_name = 'reviews'
urlpatterns = [
    url(r'^$', views.ReviewsView.as_view(), name='reviews'),
    url(r'^all/', views.ReviewsCreate.as_view(), name='create'),
]