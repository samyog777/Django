from django.urls import path

from . import views #import the view file form . (current directory)

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("samyog", views.samyog, name="samyog")
]
