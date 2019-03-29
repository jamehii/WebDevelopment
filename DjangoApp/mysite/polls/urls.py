from django.urls import path
from polls.urls import views

urlpatterns = [
    path("", views.index, name = "index")
]