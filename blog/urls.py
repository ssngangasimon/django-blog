from django.contrib.auth import views as auth_views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('new/', views.create_post, name='create_post'),
    path('<int:id>/', views.post_detail, name='post_detail'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.signup, name='signup'),  # add here

]
