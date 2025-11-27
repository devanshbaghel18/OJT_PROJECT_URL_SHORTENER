from django.urls import path
from . import views
from .views import ShortenerAPIView 

urlpatterns = [
    path('', views.home_view, name='home'),
    # This captures the short code (e.g., /A1B2C3)
    path('signup/', views.signup_view, name='signup'),    
    path('login/', views.custom_login_view, name='login'), 
    path('logout/', views.custom_logout_view, name='logout'),
    path('<str:short_code>', views.redirect_url_view, name='redirect'),
    
    # Below- Web views
    path('', views.index, name='index'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
    
    # Below- API endpoint 
    path('api/links/', ShortenerAPIView.as_view(), name='api_links'),
]