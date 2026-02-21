from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product


# REGISTER VIEW
def register_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)
        return redirect("product_list")

    return render(request, "register.html")


# LOGIN VIEW
def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,
                            username=username,
                            password=password)

        if user is not None:
            login(request, user)
            return redirect("product_list")
        else:
            return render(request, "login.html",
                          {"error": "Invalid credentials"})

    return render(request, "login.html")


# LOGOUT VIEW
def logout_view(request):
    logout(request)
    return redirect("login")


# PRODUCT LIST VIEW
@login_required
def product(request):

    products = Product.objects.all()

    return render(request,
                  "product.html",
                  {"products": products})


# PRODUCT DETAIL VIEW
@login_required
def product_detail(request, id):

    product = get_object_or_404(Product, id=id)

    return render(request,
                  "product_detail.html",
                  {"product": product})