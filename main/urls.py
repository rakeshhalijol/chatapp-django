from django.urls import path
from . import views
urlpatterns = [
    path('',views.login),
    path('signin/',views.signin),
    path('logout/',views.logout),
    path('chat/',views.chat)
]