from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("anasayfa", views.home),
    path("sutUrunlerı", views.sutUrunlerı),
     path("sutler", views.sutler),
    path("baklagıller", views.baklagıller),
    path("atıstırmalıklar", views.atıstırmalıklar),
    path("makarnalar", views.makarnalar),
    path("laktozsuzSut", views.laktozsuzSut),
    path("glutensizSut", views.glutensizSut)
    

]

