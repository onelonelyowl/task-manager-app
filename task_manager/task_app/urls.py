from django.urls import path, include
from . import views
from task_app.views import TaskCreateView

app_name = "task_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # list view
    path("<int:pk>", views.DetailView.as_view(), name="detail"),
    # detail view
    path("<int:pk>/update", views.UpdateView.as_view(), name="update"),
    path("create", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/delete", views.DeleteView.as_view(), name="delete"),

]