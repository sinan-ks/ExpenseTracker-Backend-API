"""
URL configuration for ExpenseTracker project.

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
from django.contrib import admin
from django.urls import path

from budget import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/register/', views.SignUpView.as_view()),

    path('api/expenses/', views.ExpenseListCreateView.as_view()),
    path('api/expenses/<int:pk>/', views.ExpenseDetailUpdateDestroyView.as_view()),

    path('api/incomes/', views.IncomeListCreateView.as_view()),
    path('api/incomes/<int:pk>/', views.IncomeDetailUpdateDestroyView.as_view()),

    path('api/summary/', views.TransactionSummaryView.as_view()),
    
]
