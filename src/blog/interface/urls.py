from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("posts/<str:id>/", views.UpdateDeleteRetrievePostAPIView.as_view(), name="update-delete-retrieve"),
    path("posts/", views.ListCreatePostAPIView.as_view(), name="list-or-create")
]
