from django.urls import path
from django.contrib.auth import views
from .views import UserLoginForm, signup

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
            ),
        name='login'
    ),
    path("register/", signup, name="register"),
]