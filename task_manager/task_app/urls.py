from django.urls import path, include
from . import views
from task_app.views import TaskCreateView,  task_detail, delete_comment, complete_task

app_name = "task_app"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("completed", views.IndexViewCompleted.as_view(), name="index_completed"),
    # list view
    path("<int:pk>", task_detail, name="detail"),
    # detail view
    path("users/<int:pk>", views.UserDetailView.as_view(), name="user_detail"),
    path("<int:pk>/update", views.UpdateView.as_view(), name="update"),
    path("create", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/delete", views.DeleteView.as_view(), name="delete"),
    path("<int:pk>/complete", complete_task, name="complete"),
    # path("users/<int:pk>/update", user_update, name="user_update"),
    path("users/<int:pk>/update", views.UserUpdateView.as_view(), name="user_update"),
    # https://stackoverflow.com/questions/68592568/how-to-delete-model-data-on-button-click-django
    # need to add a route for deleting comments from the detail page
    path("<int:pk>/delete_comment/<int:comment_id>", delete_comment, name="delete_comment")
]