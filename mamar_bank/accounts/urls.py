from django.urls import path,include
from accounts.views import UserRegistrationView,UserLoginView,UserLogout,UserUpdateView
urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogout.as_view(),name='logout'),
    path('profile/',UserUpdateView.as_view(),name='profile'),
]
