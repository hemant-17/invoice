from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signin/',views.signin,name='signin'),
    path('login/',views.login,name='login'),
    path('login/logout/',views.logout,name='logout'),
    path('login/invoice/',views.InvoiceListView.as_view()),
    path('login/wallet/',views.wallet,name='wallet'),
    path('login/handlerequest/', views.handlerequest, name='handlerequest'),
    path('login/outstanding/',views.outstanding,name='outstanding'),
   # path('login/add_money/',views.add_money,name='add_money'),
   # path('login/advancepay/',views.advancepay,name='advancepay'),
   #path('login/passbook/',views.passbook,name='passbook'),
   path('login/passbook/',views.PassbookListView.as_view()),
   path('login/settle_invoice/',views.Invoice_settleListView.as_view()),

]
