from django.urls import path
from . import views

urlpatterns = [
        path('', views.base, name='base'),
        path('index/', views.index, name='index'),
        path('about/', views.about, name='about'),
        path('cart/', views.cart, name='cart'),
        path('profile/', views.profile, name='profile'),
        path('contact/', views.contact, name='contact'),
        path('submit/', views.submit, name='submit'),
        path('thankyou/', views.thank_you, name='thank_you'),
        path('404error/', views.error, name='404error'),
        path('Products/', views.products, name='products'),
        path('Products/charcoal/', views.charcoal, name='charcoal'),  
        path('Products/oil', views.oil, name='oil'),
        path('Products/kitchen', views.kitchen, name='kitchen'),
        path('Products/food', views.food, name='food'),

    ]
