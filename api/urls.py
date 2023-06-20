import os
from django.urls import include, path
from rest_framework import routers

from api import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path(r'api/noticias/consultar', views.Consulta)
]