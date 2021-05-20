from django.urls import path
from . import views

urlpatterns = [
    path('chat/<str:uid>',views.home)

]
