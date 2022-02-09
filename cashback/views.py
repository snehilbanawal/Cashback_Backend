import email
from http.client import HTTPResponse
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages, auth
from accounts.models import Account
import requests
from django.contrib.auth.decorators import login_required
from .models import cashbackus, feedbackus

# Create your views here.


def home(request):

    return render(request, 'cashback/index.html')


def feedback(request):
    return render(request, 'cashback/index.html')

def footer(request):
    return render(request, 'cashback/footer.html')

def cashback(request):
  if request.user.is_admin:
    # if request.method =='POST':
    users = Account.objects.all()
    return render(request, 'cashback/cashback.html', {'users': users})
  else:
    return redirect('error')

def withdraw(request):
  if request.user.is_admin:
    # if request.method =='POST':
    users = Account.objects.all()
    return render(request, 'cashback/withdraw.html', {'users': users})
  else:
    return redirect('error')

def withdraw2(request):
  if request.user.is_admin:
    
    return render(request, 'cashback/withdraw2.html')
  else:
    return redirect('error')

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('feedback')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'cashback/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def signup(request):
    return render(request, 'cashback/signup.html')


def navbar(request):
    return render(request, 'cashback/navbar.html')



def error(request):
    return render(request, 'cashback/error.html')

def cashbackform(request):
    if request.method == 'POST':
        name1 = request.POST['name1']
        num1 = request.POST['num1']
        amount1 = request.POST['amount1']
       
        # services1 = request.POST['services1']

        cont_obj = cashbackus(name=name1, num=num1, amount=amount1)
        cont_obj.save()
        use = Account.objects.get(email=name1)
        use.cashback = use.cashback+int(amount1) #See if this works
        use.save()
        return redirect('cashback')
    else:
        return redirect('/')
 


def feedbackform(request):
    if request.method == 'POST':
        ratingg = request.POST['ratingg']
        recommendation1 = request.POST['recommendation1']
        service1 = request.POST['service1']
        message1 = request.POST['message1']
       
        # services1 = request.POST['services1']

        cont_obj = feedbackus(rating=ratingg, recommendation=recommendation1, service=service1,msg=message1)
        cont_obj.save()

        return redirect('feedback')
    else:
        return redirect('/')



def withdrawform(request):
 
    if request.method == 'POST':
        name1 = request.POST['name1']
        use = Account.objects.get(email=name1)
        
        return render(request,'cashback/withdraw2.html', {'use': use})
    else:
        return redirect('/')


def withdrawform2(request):
 
    if request.method == 'POST':
        name1 = request.POST['name1']
        amount1 = request.POST['amount1']
        amount2 = request.POST['amount2']

        famount=int(amount1)-int(amount2)
        # Account.objects.get(email='name1').update(cashback=famount)
        if famount>=0:
            q = Account.objects.get(email=name1)
            q.cashback = famount
            q.save()
            c = cashbackus.objects.get(name=name1)
            c.amount = famount
            c.save()

        
        return render(request,'cashback/withdraw2.html')
    else:
        return redirect('/')


 