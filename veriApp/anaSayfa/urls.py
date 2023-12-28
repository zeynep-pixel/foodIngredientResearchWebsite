from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("anasayfa", views.home),
    path("sutUrunlerı", views.sutUrunlerı),
    path("sutler", views.sutler),
    path("yogurtlar", views.yogurtlar),
    path("peynirler", views.peynirler),
    path("atıştırmalıklar", views.atıştırmalıklar),
    path("çikolatalar", views.çikolatalar),
    path("cipsler", views.cipsler),
    path("bisküviler", views.bisküviler)
  
  
    
    

]

