from django.urls import path
from authapp import views

urlpatterns = [
    path('',views.Home,name="index.html")

]
