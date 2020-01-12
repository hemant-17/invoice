from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('invoice/',views.InvoiceListView.as_view()),
    path('wallet/',views.wallet,name='wallet'),
    path('outstanding/',views.outstanding,name='outstanding'),
    path('advancepay/',views.advancepay,name='advancepay'),

]
