from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.myorders, name='dashboard'),
    path('myprofile/', views.userprofile, name='userprofile'),
    path('myorders/', views.myorders, name='myorders'),
    path('mypayments/', views.mypayments, name='mypayments'),
    path('useredit/', views.edit_profile, name='edit_profile'),
    path('', views.myorders, name='dashboard'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    path('password/', views.change_password, name='change_password'),
    path('orders/<id>/', views.order_details, name='order_details'),

]
