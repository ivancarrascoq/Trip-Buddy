"""TripBuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app import views
#from django.contrib.auth import views as auth_views
#from django.contrib.auth import authenticate, login, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('logout', views.logout_view, name='logout'),
    #path('logout', 'django.contrib.auth.views.logout', name='logout'),
    path('signup', views.signup, name='signup'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('trips/edit/<int:id>', views.edit, name='edit'),
    path('trips/remove/<int:id>', views.remove, name='remove'),
    path('trips/cancel/<int:id>', views.cancel, name='cancel'),
    path('trips/join/<int:id>', views.join, name='join'),
    path('trips/new', views.new, name='new_trip'),
    path('post_trip', views.post_trip, name='post_trip'),
    path('post_edit/<int:id>', views.post_edit, name='post_edit'),
    path('trips/<int:id>', views.show, name='show'),
#    path('login/', views.login_view, name='login'),

]
