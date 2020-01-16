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
    path(r'^login/invoice/$',views.InvoiceListView.as_view()),
    path(r'^login/wallet/$',views.wallet,name='wallet'),
    #path(r'^login/wallet/$',views.WalletListView.as_view()),
    path(r'^login/handlerequest/$', views.handlerequest, name='handlerequest'),
    path(r'^login/outstanding/$',views.outstanding,name='outstanding'),
    #path(r'^login/add_money/$',views.add_money,name='add_money'),
   # path(r'^login/advancepay/$',views.advancepay,name='advancepay'),
   #path(r'^login/passbook/$',views.passbook,name='passbook'),
   path(r'^login/passbook/$',views.PassbookListView.as_view()),
   path(r'^login/settle_invoice/$',views.Invoice_settleListView.as_view()),
   path(r'^login/settle/$',views.Invoice_settleListView.settle,name='settle'),
   #path(r'^login/final_settle/$',views.final_settle,name='final_settle'),

]
