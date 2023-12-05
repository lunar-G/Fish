from django.contrib import admin
from django.urls import path, include

from User import views

urlpatterns = [
    path('Login/', views.login),
    path('GetDatas/', views.getDatas),
    path('Register/', views.register),
    path('Save/', views.save),
    path('Delete/', views.delete),
    path('Admin/', views.admin),
    path('PersonalInfo/', views.personalInfo),
    path('Merchant/', views.getMerchants),
    path('Account/', views.getAccount),
    path('ShopControl/', views.shopControl),
    path('Reply/', views.reply),
    path('Audit/', views.audit),
    path('AccControl/', views.accControl),
    path('InfoDelete/', views.infoControl),
    path('BuyAndCart/', views.buyAndCart),
    path('SendMessage/',views.sendMessage),
    path('Settlement/', views.settlement)
]
