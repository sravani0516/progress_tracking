from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='home'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('product/', views.product, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product-detail'),

]