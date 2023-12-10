from django.urls import path, include
from . import views
from task_app.views import TaskCreateView, user_update, task_detail

app_name = "task_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # list view
    path("<int:pk>", task_detail, name="detail"),
    # detail view
    path("users/<int:pk>", views.UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/update", views.UpdateView.as_view(), name="update"),
    path("create", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/delete", views.DeleteView.as_view(), name="delete"),
    path("users/<int:pk>/update", user_update, name="user_update"),

]