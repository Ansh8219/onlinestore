from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.hashers import make_password



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
# signup here
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        hashed_password = make_password(password)

        # Use create_user to handle password hashing
        User.objects.create_user(username=username, email=email, password=hashed_password)

        # Optionally, you can log in the user after registration
        # You need to import login function from django.contrib.auth
        # login(request, user)

        messages.success(request, 'User has successfully been created')
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')
# login here
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'you are succesfully login in ')
            return render(request, "index.html")
        else:
            messages.error(request,'Invalid User')
            return redirect('login')
    else:
        return render(request, "login.html")

