from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_page),
    path('<path:menu_path>/', views.test_page),

]
