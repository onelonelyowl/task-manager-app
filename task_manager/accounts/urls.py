from django.urls import path
from django.contrib.auth import views
from .views import RegisterView, UserLoginForm

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
    ),
    path("register/", RegisterView.as_view(), name="register"),
]