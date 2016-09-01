from django.conf.urls import url
from . import views

app_name = "api"

urlpatterns = [
    url(r'^v0/data$', views.data, name='data')
]
