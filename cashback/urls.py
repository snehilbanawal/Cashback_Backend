from django.urls import path

from . import views
from accounts import views as acc_views

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('cashback/', views.cashback, name='cashback'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myprofile/', acc_views.userprofile, name='userprofile'),
    path('editprofile/', acc_views.edit_profile, name='editprofile'),
    path('register/', acc_views.register, name='register'),
    path('navbar/', views.navbar, name='navbar'),
    path('footer/', views.footer, name='footer'),
    path('', views.home, name='home'),
    path('cashbackform', views.cashbackform, name='cashbackform'),
    path('feedbackform', views.feedbackform, name='feedbackform'),
    path('error', views.error, name='error'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('withdraw2', views.withdraw2, name='withdraw2'),
    path('withdrawform', views.withdrawform, name='withdrawform'),
    path('withdrawform2', views.withdrawform2, name='withdrawform2'),
]
