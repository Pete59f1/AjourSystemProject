from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # path('', views.indexView, name='home'),
    # path('register/', views.registerView, name='register_url'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('', LoginView.as_view(template_name='login.html'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout')
]
