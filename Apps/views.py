from django.shortcuts import render
from django.contrib import messages
from .models import Employee
from .models import Feedback
from .models import Loan_apply
from .models import Login_user
from .models import Signup_user

from django.http import HttpResponse
# Create your views here.
def base(request):
    return render(request,"base.html")

def contactus(request):

    if request.method == "POST":
        NAME_AS_ON_PANCARD=request.POST.get(' NAME_AS_ON_PANCARD')
        PERSONAL_EMAIL_ID=request.POST.get('PERSONAL_EMAIL_ID')
        MOBILE_NUMBER=request.POST.get('MOBILE_NUMBER')
        SUBJECT_LINE=request.POST.get('SUBJECT_LINE')
        Write_Message=request.POST.get('Write_Message')
        en=Feedback(NAME_AS_ON_PANCARD=NAME_AS_ON_PANCARD,PERSONAL_EMAIL_ID=PERSONAL_EMAIL_ID,MOBILE_NUMBER=MOBILE_NUMBER,SUBJECT_LINE=SUBJECT_LINE,Write_Message=Write_Message)
        en.save()
        
        return HttpResponse('Employed added successfully')
    elif request.method =='GET':
        return render(request, 'contactus.html')
    
    else:
        return HttpResponse("An exception occurred while processing")
 
def homepage(request):

    data={
        'title':'Home Page'
    }

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = int(request.POST.get('amount'))
        term = int(request.POST.get('term'))
        new_empl = Loan_apply(name=name,email=email,amount=amount,term=term)
        new_empl.save()
        return HttpResponse('Loan Application Successfully In User')
    elif request.method =='GET':
        return render(request, 'home.html')
    
    else:
        return HttpResponse("An exception occurred while processing")

def service(request):
    return render(request,"service.html")


def aboutus(request):
    return render(request,"aboutus.html")

def news(request):
    return render(request,"news.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = int(request.POST.get('password'))
        new_user = Login_user(username=username,password=password)
        new_user.save()
        
        return HttpResponse('New user Login successful Add Welcome to Money Sutra Loan Application')
        
    elif request.method =='GET':
        return render(request, 'login.html')
    
    else:
        return HttpResponse("An exception occurred while processing")


def learn(request):
    return render(request,"learn.html")

def peages(request):
    return render(request,"peages.html")


def applyloan(request):
    return render(request,"applyloan.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        Email = request.POST.get('Email')
        password = int(request.POST.get('password'))
        Confirm_Password = int(request.POST.get('password'))
        new_users = Signup_user(username=username,Email=Email,password=password,Confirm_Password=Confirm_Password)
        new_users.save()
        return HttpResponse('New user Signup User successful Add Welcome to Money Sutra Loan Application')
    elif request.method =='GET':
        return render(request, 'signup.html')
    
    else:
        return HttpResponse("An exception occurred while processing")

def payments(request):
    return render(request,"payments.html")

def document(request):
    return render(request,"document.html")

def calculoter(request):
    return render(request,"calculoter.html")


def faqs(request):
    return render(request,"faqs.html")


def bussiness(request):
    return render(request,"bussiness.html")

def cibil(request):
    return render(request,"cibil.html")

def cards(request):
    return render(request,"cards.html")

def personal(request):
    return render(request,"personal.html")

def banking(request):
    return render(request,"banking.html")

def how_apply(request):
    return render(request,"how_apply.html")

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        salary = int(request.POST.get('salary'))
        dept = int(request.POST.get('dept'))
        role = int(request.POST.get('role'))
        bonus = int(request.POST.get('bonus'))
        new_emp = Employee(name=name, last_name=last_name, salary=salary, dept=dept, role=role, bonus=bonus)
        new_emp.save()
        messages.success(request, "YOUR MESSAGE ")
        return HttpResponse('Employed added successfully')
    elif request.method =='GET':
        return render(request, 'form.html')
    
    # else:
    #     return HttpResponse("An exception occurred while processing")
    

def cricket(request):
    return render(request, 'cricket.html')