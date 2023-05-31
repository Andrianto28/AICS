from django.urls import path
from . import views

urlpatterns =[
    path("cobaa/",views.cobaa, name= "cobaa"),
    path("ping/", views.ping, name ="ping"), 

    # (1) inputting automation
    path("ocrnib/", views.ocrnib, name="ocrnib"),
    path("ocrsiup/", views.ocrsiup, name="ocrsiup"),
    path("ocrtdp/", views.ocrtdp, name="ocrtdp"),
    path("ocrskdp/", views.ocrskdp, name="ocrskdp"),
    path("ocrnpwp/", views.ocrnpwp, name="ocrnpwp")
]