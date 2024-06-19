
from django.urls import path
from . import views
urlpatterns = [

    path("",views.chai, name="chai"),
]
