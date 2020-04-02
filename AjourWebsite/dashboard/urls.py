from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    # path('login/', name='blaa'),
    # path('logout/', name='bloo'),
    # path('register/', name='flob')
]
