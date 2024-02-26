from django.shortcuts import render, redirect
from Backend.models import ProdcutDB, CategoryDB, BlogDB
from Frontend.models import ContactDB, UserRegistrationDB, cartDB, CheckoutDB
from django.contrib import messages


# Create your views here.
def Homepage(request):
    products = ProdcutDB.objects.all()
    categories = CategoryDB.objects.all()
    return render(request, 'HomePage.html', {'products': products, 'categories': categories})


def ProductsPage(request, catname):
    prod = ProdcutDB.objects.filter(CATEGORY=catname)
    categories = CategoryDB.objects.all()
    return render(request, 'Products.html', {'prod': prod, 'categories': categories})


def AboutPage(request):
    categories = CategoryDB.objects.all()
    return render(request, 'AboutPage.html',{'categories': categories})


def ContactPage(request):
    categories = CategoryDB.objects.all()
    return render(request, 'ContactPage.html', {'categories': categories})


def SingleProduct(request, proid):
    categories = CategoryDB.objects.all()
    product = ProdcutDB.objects.get(id=proid)
    return render(request, 'SingleProduct.html', {'product': product, 'categories': categories})


def ContactPage_save(request):
    if request.method == 'POST':
        nm = request.POST.get('Name')
        email = request.POST.get('Email')
        sub = request.POST.get('Subject')
        message = request.POST.get('Message')
        obj = ContactDB(NAME=nm, EMAIL=email, SUBJECT=sub, MESSAGE=message)
        obj.save()
        return redirect(ContactPage)


def SignUpLoginPage(request):
    return render(request, 'User_Login.html')


def UserRegistrationDBsave(request):
    if request.method == "POST":
        nm = request.POST.get('SignUpName')
        email = request.POST.get('Email')
        pwd = request.POST.get('SignUpPassword')
        pwd1 = request.POST.get('ConfirmPassword')
        if pwd == pwd1:
            if UserRegistrationDB.objects.filter(NAME=nm).exists():
                messages.info(request, "UserName already exists")
                return redirect(SignUpLoginPage)
            elif UserRegistrationDB.objects.filter(EMAIL=email).exists():
                messages.info(request, "Email already exists")
            else:
                obj = UserRegistrationDB(NAME=nm, EMAIL=email, PASSWORD=pwd)
                obj.save()
                return redirect(SignUpLoginPage)
        else:
            messages.info(request, "Passwords does not match")
            return redirect(SignUpLoginPage)
def UserLogin(request):
    if request.method == "POST":
        unm = request.POST.get('LoginName')
        email = request.POST.get('LoginEmail')
        pwd = request.POST.get('LoginPassword')
        if UserRegistrationDB.objects.filter(NAME=unm, PASSWORD=pwd, EMAIL=email).exists():
            request.session['NAME'] = unm
            request.session['EMAIL'] = email
            request.session['PASSWORD'] = pwd
            return redirect(Homepage)
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect(SignUpLoginPage)
    else:
        return redirect(SignUpLoginPage)


def UserLogout(request):
    del request.session['NAME']
    del request.session['PASSWORD']
    del request.session['EMAIL']
    return redirect(SignUpLoginPage)


def FrontendBlog(request):
    blog = BlogDB.objects.all()
    categories = CategoryDB.objects.all()
    return render(request, 'FrontendBlog.html', {'blog': blog, 'categories': categories})


def BlogSingle(request, blogid):
    blog = BlogDB.objects.get(id=blogid)
    categories = CategoryDB.objects.all()
    return render(request, 'BlogSingle.html', {'blog': blog,'categories': categories})


def cartDBsave(request):
    if request.method == "POST":
        usrnm = request.POST.get("usrname")
        productnm = request.POST.get("proname")
        productprice = request.POST.get("proprice")
        Quant = request.POST.get("qnty")
        TotalPr = request.POST.get("totalprice")
        obj = cartDB(Username=usrnm, Productname=productnm, Price=productprice, Quantity=Quant, Totalprice=TotalPr)
        obj.save()
        messages.success(request, "Added to Cart Successfully")
        return redirect(Homepage)

def cart_page(request):
    categories = CategoryDB.objects.all()
    cart = cartDB.objects.filter(Username=request.session['NAME'])
    total_price = 0
    for i in cart:
        total_price = total_price + i.Totalprice
    return render(request, 'cart.html', {'cart':cart, 'total_price':total_price, 'categories':categories})

def cartDelete(request,cartid):
    cart = cartDB.objects.filter(id=cartid)
    cart.delete()
    return redirect(cart_page)

def Checkout(request):
    categories = CategoryDB.objects.all()
    cart = cartDB.objects.filter(Username=request.session['NAME'])
    total_price = 0
    for i in cart:
        total_price = total_price + i.Totalprice
    return render(request, 'Checkout.html', {'cart':cart, 'total_price':total_price, 'categories':categories})

def CheckoutDBsave(request):
    if request.method == "POST":
        nmfirst = request.POST.get('firstname')
        nmlast = request.POST.get('lastname')
        countr = request.POST.get('country')
        addr = request.POST.get('address')
        city1 = request.POST.get('city')
        pncode = request.POST.get('pincode')
        mob = request.POST.get('mobile')
        Em = request.POST.get('email')
        obj = CheckoutDB(firstnm=nmfirst, lastnm=nmlast, country=countr, address=addr, city=city1, pincode=pncode,
                         phone=mob, email=Em)
        obj.save()
        messages.success(request, "Order Placed Successfully")
        return redirect(Checkout)
