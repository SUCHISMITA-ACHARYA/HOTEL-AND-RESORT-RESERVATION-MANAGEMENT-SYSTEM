from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("Home", views.home, name="Home"),
   
    path("<int:id>",views.detail, name = "booking"),
    path("create/", views.create, name="create"),
    path("create/form/<int:id>",views.index, name = "INDEX"),
   

]
