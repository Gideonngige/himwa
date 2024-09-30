from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from himwaApp.form import Login, Register, SearchForm
from . models import Login2
from django.core.mail import send_mail
from django.conf import settings
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
def home(request):
    loginForm = Login(request.POST)
    if loginForm.is_valid():
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            if Login2.objects.filter(email=email, password=password).exists():
                messages.info(request, 'Successful login!')
                user = Login2.objects.get(email=email)
                user_name = user.name 
                user_phone = user.phone_number
                user_email = user.email
                user_bill = user.bill
                user_paid = user.paid
                january_bill = user.january
                february_bill = user.february
                march_bill = user.march
                request.session['user_name'] = user_name 
                request.session['user_phone'] = user_phone
                request.session['user_email'] = user_email
                request.session['user_bill'] = user_bill
                request.session['user_paid'] = user_paid
                request.session['january_bill'] = january_bill
                request.session['february_bill'] = february_bill
                request.session['march_bill'] = march_bill
                return redirect('profile')
            else:
                messages.info(request, 'Invalid inputs!')
    return render(request, 'home.html', {'loginForm':loginForm}) 

#register function 
def register(request):
    registerForm = Register(request.POST)
    if registerForm.is_valid():
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            if Login2.objects.filter(email=email).exists():
                messages.info(request, 'Email exists!')
            elif password == password2:
                user_register = Login2(name=name,email=email,phone_number=phone_number, password=password)
                user_register.save()
                subject = 'Welcome to Himwa'
                message = f'Hi {email}, thank you for registering, you are a Himwa member now'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['gideonushindi94@gmail.com', ]
                send_mail( subject, message, email_from, recipient_list)
                return redirect('home')
    return render(request, 'register.html', {'registerForm':registerForm})

#user profile function
def profile(request):
    user_name = request.session.get('user_name', None)
    user_phone = request.session.get('user_phone', None)
    user_email  = request.session.get('user_email', None)
    user_bill  = request.session.get('user_bill', None)
    user_paid  = request.session.get('user_paid', None)
    january_bill = request.session.get('january_bill', None)
    february_bill = request.session.get('january_bill', None)
    march_bill = request.session.get('january_bill', None)
    balance = user_bill - user_paid
    return render(request, 'profile.html',{'user_name':user_name, 'user_phone':user_phone, 'user_email':user_email,'user_bill':user_bill,'user_paid':user_paid,'balance':balance,'january_bill':january_bill,'february_bill':february_bill,'march_bill':march_bill})

#make payment function
def payment(request):
    user_phone = request.session.get('user_phone', None)
    user_bill  = request.session.get('user_bill', None)
    if request.method == 'POST':
        cl = MpesaClient()
        phone_number = user_phone
        amount = user_bill
        account_reference = '174379'
        transaction_desc = 'Pay for G-Tech Services'
        callback_url = 'https://api.darajambili.com/express-payment'
        response = cl.stk_push(phone_number, amount, account_reference,
        transaction_desc, callback_url)
        return HttpResponse(response)
#function for members
def members(request):
    users = Login2.objects.values()
    search_form = SearchForm(request.POST)
    if request.method == 'POST':
       try: 
        search = request.POST.get('search')
        user_search = Login2.objects.get(name=search)
        user_search_result = user_search.name + ' is present at row ' + str(user_search.id)
        return render(request, 'members.html', {'search_form':search_form,'users':users,'user_search_result':user_search_result})
       except Login2.DoesNotExist:
           user_search_result = 'Absent'
           return render(request, 'members.html', {'search_form':search_form,'users':users,'user_search_result':user_search_result})
    return render(request, 'members.html', {'users':users})