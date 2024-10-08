"""
URL configuration for django_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departments_list, name='departments_list'),
    path('elevators/', views.elevators_list, name='elevators_list'),
    path('doors/', views.doors_list, name='doors_list'),
    # path('get-steps/<str:department_name>/', views.get_steps, name='get-steps'),
    path('department_names/', views.department_names, name='departments'),
    path('get_department/<str:department_name>/', views.get_department, name='get_department'),
    path('closest_door/<str:department_name>/', views.get_closest_door, name='get_closest_door'),
    path('closest_parking_lot/<str:department_name>/<int:closest_door>/', views.get_closest_parking_lot, name='get_closest_parking_lot'),
    path('generate_steps_nsp/<str:department_name>/', views.generate_steps_nsp, name='generate_steps_nsp'),
    path('unity_steps_nsp/<str:department_name>/', views.unity_steps_nsp, name='unity_steps'),
    path('generate_steps_dd/<str:start_point>/<str:destination>/', views.generate_steps_dd, name='generate_steps_dd'),
    path('unity_steps_dd/<str:start_point>/<str:destination>/', views.unity_steps_dd, name='unity_steps_dd')
]
