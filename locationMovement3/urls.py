from django.urls import path
from . import views

urlpatterns =[
    path("predictloc/", views.predictloc, name="predictloc")
]