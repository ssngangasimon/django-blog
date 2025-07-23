from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name='about'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]
