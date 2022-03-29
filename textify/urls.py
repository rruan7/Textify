from django.urls import path
from . import views

urlpatterns = [
    # link root app URL to textify view
    path("", views.TextifyView.textify_view, name="textify_view"),
    path("<int:id>", views.TextifyView.update_textify, name="update_textify"),
]