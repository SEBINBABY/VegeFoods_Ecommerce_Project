from django.shortcuts import render, redirect
from Backend.models import CategoryDB, ProdcutDB, BlogDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from Frontend.models import ContactDB
from django.contrib import messages

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def AddCategory(request):
    return render(request, 'AddCategory.html')

def categorysave(request):
    if request.method == 'POST':
        nm = request.POST.get('Name')
        desc = request.POST.get('Description')
        img = request.FILES['Image']
        obj = CategoryDB(NAME=nm, DESC=desc, IMAGE=img)
        obj.save()
        messages.success(request, "Category Saved Successfully")
        return redirect(AddCategory)

def displaycat(request):
    category = CategoryDB.objects.all()
    return render(request, 'Display.html', {'category':category})

def editcategory(request, catid):
    category = CategoryDB.objects.get(id=catid)
    return render(request, 'EditCategory.html', {'category':category})

def updatecategory(request, catid):
    if request.method == 'POST':
        nm = request.POST.get('Name')
        desc = request.POST.get('Description')
        try:
            img = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=catid).IMAGE
        CategoryDB.objects.filter(id=catid).update(NAME=nm, DESC=desc, IMAGE=file)
        messages.success(request, "Category Updated Successfully")
        return redirect(displaycat)

def deletecategory(request, catid):
    category = CategoryDB.objects.filter(id=catid)
    category.delete()
    messages.error(request, "Category is Deleted")
    return redirect(displaycat)

def AddBlog(request):
    return render(request, 'AddBlog.html')

def Blogsave(request):
    if request.method == 'POST':
        date = request.POST.get('Date')
        title = request.POST.get('Title')
        s_desc = request.POST.get('ShortDescription')
        f_desc = request.POST.get('FullDescription')
        image = request.FILES['Image']
        obj = BlogDB(DATE=date, TITLE=title, SHORTDESC=s_desc, FULLDESC=f_desc, IMAGE=image)
        obj.save()
        messages.success(request, "Blog Saved Successfully")
        return redirect(AddBlog)

def BlogDisplay(request):
    blog = BlogDB.objects.all()
    return render(request, 'BlogDisplay.html', {'blog':blog})

def editblog(request, blogid):
    blog = BlogDB.objects.get(id=blogid)
    return render(request, 'EditBlog.html', {'blog':blog})

def updateblog(request, blogid ):
    if request.method == 'POST':
        date = request.POST.get('Date')
        title = request.POST.get('Title')
        s_desc = request.POST.get('ShortDescription')
        f_desc = request.POST.get('FullDescription')
        try:
            image = request.FILES['Image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = BlogDB.objects.get(id=blogid).IMAGE
        BlogDB.objects.filter(id=blogid).update(DATE=date, TITLE=title, SHORTDESC=s_desc, FULLDESC=f_desc, IMAGE=file)
        messages.success(request, "Blog Updated Successfully")
        return redirect(BlogDisplay)

def deleteblog(request, blogid):
    blog = BlogDB.objects.filter(id=blogid)
    blog.delete()
    messages.error(request, "Blog is Deleted")
    return redirect(BlogDisplay)



def AddProduct(request):
    category = CategoryDB.objects.all()
    return render(request, 'AddProduct.html', {"category":category})

def productsave(request):
    if request.method == 'POST':
        catnm = request.POST.get('CatName')
        pronm = request.POST.get('ProName')
        proprice = request.POST.get('ProPrice')
        prodesc = request.POST.get('ProDesc')
        proimg = request.FILES['ProImage']
        obj = ProdcutDB(CATEGORY=catnm, PRONAME=pronm, PROPRICE=proprice, PRODESC=prodesc, PROIMAGE=proimg)
        obj.save()
        messages.success(request, "Product Saved Successfully")
        return redirect(AddProduct)

def displayproduct(request):
    product = ProdcutDB.objects.all()
    return render(request, 'DisplayProduct.html', {'product':product})

def editproduct(request, proid):
    product = ProdcutDB.objects.get(id=proid)
    category = CategoryDB.objects.all()
    return render(request, 'EditProduct.html', {'product':product, 'category':category})

def updateproduct(request, proid):
    if request.method == 'POST':
        catnm = request.POST.get('CatName')
        pronm = request.POST.get('ProName')
        prodesc = request.POST.get('ProDesc')
        try:
            img = request.FILES['ProImage']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProdcutDB.objects.get(id=proid).PROIMAGE
        ProdcutDB.objects.filter(id=proid).update(CATEGORY=catnm, PRONAME=pronm, PRODESC=prodesc, PROIMAGE=file)
        messages.success(request, "Product Updated Successfully")
        return redirect(displayproduct)

def deleteproduct(request, proid):
    product = ProdcutDB.objects.filter(id=proid)
    product.delete()
    messages.error(request, "Product is Deleted")
    return redirect(displayproduct)

def admin_login_page(request):
    return render(request, 'AdminLogin.html')

def AdminLogin(request):
    if request.method == 'POST':
        unm = request.POST.get('uname')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=unm).exists():
            user = authenticate(username=unm, password=pwd)
            if user is not None:
                login(request, user)
                request.session['username'] = unm
                request.session['password'] = pwd
                messages.success(request, "Logged In Successfully")
                return redirect('indexpage')
            else:
                messages.error(request, "Inavalid Username or Password")
                return redirect('admin_login_page')
        else:
            messages.error(request, "Inavalid Username or Password")
            return redirect('admin_login_page')

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logged Out Successfully")
    return redirect('admin_login_page')

def CustomerContactDisplay(request):
    customerData = ContactDB.objects.all()
    return render(request, 'CustomerContactDisplay.html', {'customerData':customerData})

def CustomerContactDelete(request, customid):
    data = ContactDB.objects.filter(id=customid)
    data.delete()
    messages.error(request, "Customer Details are Deleted")
    return redirect(CustomerContactDisplay)


