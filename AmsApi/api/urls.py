from api import views
from django.urls import path

urlpatterns = [
    path('login', views.LoginView.as_view()),
    path('me', views.MeView.as_view()),
    path('users/<int:id>', views.UserView.as_view()),
    path('users', views.UsersView.as_view())
]