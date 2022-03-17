from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("signup/check/", views.duplicated_check, name="duplicated_check"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),   
]


