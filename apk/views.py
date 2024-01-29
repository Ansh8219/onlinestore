from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.core.mail import send_mail
# Create your views here.
def main(request):
    return render (request,'main.html')

def home(request):
    return render (request,'index.html')

def shop(request):
    return render (request,'shop.html')

def about(request):
    return render (request,'about.html')

def blog(request):
    return render (request,'blog.html')

def contact(request):
    return render (request,'contact.html')

def cart(request):
    return render (request,'cart.html')

def checkout(request):
    return render (request,'checkout.html')

def blog_single(request):
    return render (request,'blog-single.html')

def product_single(request):
    return render (request,'product-single.html')

def profile(request):
    return render (request,'profile.html')

def logsign(request):
    return render (request,'logsign.html')

def ChangePassword(request):
    return render (request,'ChangePassword.html')
# signup here
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=name, email=email, password=password)
        
        messages.success(request, 'User has successfully been created')
        
        send_mail(
            "Mail from Anshu Website",
            f"Thanks {name} for Signup with us , our team connect with you with in hour ",
            "anshu93172@gmail.com",
            [email],
            fail_silently=False,
        )
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')
# login here
def login(request):
    
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        my_user=User.objects.get(email=email).username
        user=authenticate(username=my_user,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'successfully login')           
            return render(request,"index.html") 
        else:
            messages.error(request, 'Invalid user')
            return redirect('login')
    else:
        return render(request, "login.html")

def user():
    s=User.objects.get(username=s)
    
def Logout(request):
    x=User.objects.all()
    x.logout()
    messages.success(request,'logout succesfully')
    return redirect(main)