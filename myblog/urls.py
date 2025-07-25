from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from blog import views as blog_views

urlpatterns = [
    path('', lambda request: redirect('home'), name='root'),  # redirects to /blog/
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Blog routes
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', blog_views.signup, name='signup'),
]
