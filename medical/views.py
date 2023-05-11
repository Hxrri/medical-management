from django.shortcuts import render,redirect
from.models import contact,product,Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def contact(request):
    if request.method == "POST":
        name=request.POST.get('ContactName')
        phone=request.POST.get('PhoneNumber')
        Email=request.POST.get('Email')
        addr=request.POST.get('Address')
        C=contact(ename=name,phno=phone,email=Email,address=addr)
        C.save()
    return render(request,'contact.html')



def home(request):
    return render(request,'home.html')

def userlogin(request):
    if request.method == "POST":
        uname=request.POST.get("Username")
        pass1=request.POST.get("Password")
        L=authenticate(username=uname,password=pass1)
        if L is not None:
            login(request,L)
            return redirect('/uhome')
        else:
            return redirect('/login')
    return render(request,'login.html')

def uhome(request):
    return render(request,'userhome.html')


def about(request):
    return render(request,'about.html')
def meds(request):
    a=product.objects.all()
    return render(request,'medicine.html',{'product': a})

def signup(request):
    if request.method =="POST":
        uname=request.POST.get("Username")
        firstnames=request.POST.get("fname")
        lastnames=request.POST.get("lname")
        email=request.POST.get("Email")
        password=request.POST.get("Password")
        confirmpassword=request.POST.get("Confirmpassword")
        if( password != confirmpassword):
            return redirect ('/signup')
        try:
            if User.objects.get(username=uname):
                return redirect ('/signup')
        except:    
            pass

        use=User.objects.create_user(uname,email,password)
        use.first_name=firstnames
        use.last_name=lastnames
        use.save()
        return redirect('/login')
    return render(request,'signup.html')



def order(request):
    item=product.objects.all()
    if request.method == "POST":
        name=request.POST.get('Orname')
        email=request.POST.get('email')
        items=request.POST.get('items')
        quan=request.POST.get('quantity')
        phnum=request.POST.get('phonenumber')
        addr=request.POST.get('address')
        print(name,email,items,quan)
        pri=" "
        for i in item:
            if items == i.Pname:
                pri=i.price
            pass
        newprice=int(pri)*int(quan)    
        O=Order(Oname=name,email=email,items=items,quantity=quan,poheno=phnum,address=addr,price=newprice)
        O.save()
        return redirect('/orderdetail')
    
    return render(request,'order.html',{'product': item})

def orderdetails(request):
    items=Order.objects.all()
    return render(request,'orderdetails.html',{'Order': items })

def delet(request,id):
    D=Order.objects.get(id=id)
    D.delete()
    return redirect('/orderdetail')


