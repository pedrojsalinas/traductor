from django.urls import path

from traductor.views import *

urlpatterns = [
    # path('', views.index, name='index'),
    path('', TraductorView.as_view(), name='traductor')
]
