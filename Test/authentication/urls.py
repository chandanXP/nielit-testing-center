from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('registration/', views.registration_success, name='registration_success'),
]
