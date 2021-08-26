from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.Loginview.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_views(template_name='users/logout.html'), name='logout')
]
