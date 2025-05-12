from django.urls import path

from . import views

app_name = "transactions"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.details, name="details"),
    path("add", views.add, name="add"),
    path("<int:pk>/delete/", views.delete, name="delete"),
]
