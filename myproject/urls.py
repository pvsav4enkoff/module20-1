"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from plant.views import *

urlpatterns = [
    # path('', spis),
    path('admin/', admin.site.urls),
    path('', view_plant),
    path('employees/', employee_list, name='employee_list'),
    path('employees/delete/<pk>/', delete_employee, name='delete_employee'),
    path('employees/edit/<pk>/', edit_employee, name='edit_employee'),
    # path('employees/edit/<pk>/', sign_up_by_plant2, name='edit_employee'),
    # path('plant/', view_plant),
    path('plant/employee', view_plant_employee, name='employee_main'),
    path('plant/employee/sign_up', sign_up_by_plant),

]
