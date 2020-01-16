from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User , auth
from django.contrib import messages
from . models import Customer , Invoice , Profile , Wallet
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt
from . paytm import checksum
MERCHANT_KEY = 'npI_h5KJ6!BxemZ4'
dict1 = {'order':True ,'amt':0 , 'user':'hemant'}


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,'contact.html')

def signin(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already registered')
                return redirect('signin')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect('signin')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"Confirm Password did not mathch")
            return redirect('signin')




    return render(request,"signup.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        User=auth.authenticate(username=username,password=password)

        if User is not None:
            auth.login(request ,User)
            return redirect('/')
        else:
             messages.info(request,'Invalid Credentials')
             return redirect('login')


    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


@method_decorator(login_required,name="dispatch")
class InvoiceListView(ListView):
    template_name = 'invoice.html'
    context_object_name = 'invoice_id'
    model = Invoice
    def get_queryset(self):
        #return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
        #print (Invoice.objects.filter(customer_id=1)
        #print(Invoice.objects.filter(customer_id=1))
        return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)



@method_decorator(login_required,name="dispatch")
class InvoiceDetailView(DetailView):
    model = Invoice

def wallet(request):
    def get_queryset(self):
        #return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
        #print (Invoice.objects.filter(customer_id=1)
        #print(Invoice.objects.filter(customer_id=1))
        return Wallet.objects.filter(username=self.request.user.profile.user)
    if request.method=='POST':
        invoice_id = request.POST.get('invoice_id','')
        username=request.POST.get('username','')
        email=request.POST.get('email','')
        amount=request.POST.get('amount','')
        wallet = Wallet(username=username, email=email ,amount=amount, invoice_id=invoice_id)
        wallet.save()
        print(invoice_id)
        print(amount)
        print(request.user.email)
        dict1['amt'] = amount
        dict1['user'] = request.user.username


        param_dict = {
            'MID':'AhagdK84355164141885',
            'ORDER_ID':str(invoice_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID': request.user.email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'DEFAULT',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/login/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
        #update_balance(amount)
        return render(request,'paytm.html', {'param_dict': param_dict})
    return render(request,'wallet.html')



@csrf_exempt
def handlerequest(request):
    #paytm will post request here

    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        """if i=='CHECKSUMHASH':
            checksum=form[i]

    #verify = checksum.verify_checksum(response_dict, MERCHANT_KEY)
    verify = checksum.verify_checksum(param_dict, merchant_key, checksum)
    if verify:"""
    if response_dict['RESPCODE'] =='01':
            print("Order Successsful")

            dict1['order']=True
    else:
            print("Order was not Successsful because " + response_dict['RESPMSG'])
            dict1['order']=False
            print(dict1['order'])
            #amt=120
            update_balance()
    return  render(request,"paymentstatus.html" )

def update_balance():
    print("ok")
    bal = Wallet.objects.get(username=dict1['user'])
    print(bal.balance)
    print(dict1['amt'])
    #for i in bal:
        #print(i.balance)
    if(dict1['order']==True):
        bal.balance = bal.balance + int(dict1['amt'])
        bal.save()
        print(bal.balance)
    else:
        print("No change ")
        bal.balance = bal.balance - int(dict1['amt'])

        print(bal.balance)


def outstanding(request):
   return HttpResponse("this is outstanding ")

def advancepay(request):
    return HttpResponse("this is advance pay ")

@method_decorator(login_required,name="dispatch")
class PassbookListView(ListView):
    template_name = 'passbook.html'
    context_object_name = 'username'
    model = Wallet
    def get_queryset(self):
        #return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
        #print (Invoice.objects.filter(customer_id=1)
        #print(Invoice.objects.filter(customer_id=1))
        return Wallet.objects.filter(username=self.request.user.profile.user)




@method_decorator(login_required,name="dispatch")
class WalletDetailView(DetailView):
    model = Wallet

@method_decorator(login_required,name="dispatch")
class Invoice_settleListView(ListView):
    template_name = 'settle_invoice.html'
    context_object_name = 'invoice_id'
    model = Invoice
    def get_queryset(self):
        #return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
        #print (Invoice.objects.filter(customer_id=1)
        #print(Invoice.objects.filter(customer_id=1))
        #self.resp = Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
        return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
    def settle(self):
        bal = Wallet.objects.get(username=dict1['user'])
        #resp = Invoice.objects.filter(customer_id=self.user.profile.customer_id).values_list('outstanding')
        resp = Invoice.objects.values_list('outstanding', flat=True).get(customer_id=self.user.profile.customer_id)
        #for i in invoice_id:
            #out = i.outstanding
            #print(out)
        print(resp)

        print(bal.balance)
        if(bal.balance < resp):
            messages.info(self,'Please add money in Wallet to clear your outstanding')
            return redirect('/login/wallet')
        else:
            bal.balance = bal.balance - resp
            bal.save()
            resp = 0
            pat = Invoice.objects.get(customer_id = self.user.profile.customer_id)
            pat.outstanding = resp
            pat.save()
            print(bal.balance)
            messages.info(self,'Outstanding cleared ')

            return redirect('/login/invoice')
        #return HttpResponse('Wait')



@method_decorator(login_required,name="dispatch")
class Invoice_settleDetailView(DetailView):
    model = Invoice

def passbook(request):
    return HttpResponse("this is passbook ")

#def update_balance(curr_balance):


#def amt_debit(balance):
#    if (balance<0):
#        return redirect('passbook')
#    elif (balance>0):
#       messages.info(request,'Please add money to wallet')
#       return redirect('passbook')
#   else:



    #return render(request,'wallet.html')
"""
    @method_decorator(login_required,name="dispatch")
class WalletListView(ListView):
    template_name = 'wallet.html'
    context_object_name = 'username'
    model = Invoice
    def get_queryset(self):
        #return Invoice.objects.filter(customer_id=self.request.user.profile.customer_id)
        #print (Invoice.objects.filter(customer_id=1)
        #print(Invoice.objects.filter(customer_id=1))
        return Wallet.objects.filter(username=self.request.user.profile.user)


def add_money(request):
        if request.method=='POST':
                invoice_id = request.POST.get('invoice_id','')
                username=request.POST.get('username','')
                email=request.POST.get('email','')
                amount=request.POST.get('amount','')
                wallet = Wallet(username=username, email=email ,amount=amount, invoice_id=invoice_id)
                wallet.save()

                param_dict = {
                    'MID':'AhagdK84355164141885',
                    'ORDER_ID':str(wallet.invoice_id),
                    'TXN_AMOUNT':str(amount),
                    'CUST_ID': request.user.email,
                    'INDUSTRY_TYPE_ID':'Retail',
                    'WEBSITE':'DEFAULT',
                    'CHANNEL_ID':'WEB',
                    'CALLBACK_URL':'http://127.0.0.1:8000/login/handlerequest/',




                }

#                checksum = ''
#                checksum = checksum.generate_checksum(param_dict, MERCHANT_KEY)
                param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict,MERCHANT_KEY)
                return render(request,'paytm.html', {'param_dict': param_dict})
#                return render(request,'paytm.html', {'param_dict': param_dict})
        return render(request,'/login/passbook/')

    """
