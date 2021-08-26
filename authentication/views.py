from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . import  context_processors
from .models import ProductList
from .form import MyForm
# Create your views here.

globalUser=""
def index(request):
    print('hello from den')
    return render(request,'home.html',{'name':'Denil '})

def add(request):
    print('add')
    return render(request,'home.html',{'name':'Nair '})

def home(request):
    if context_processors.dict["testme"] == 'loggedin':
            
            
            return render(request,'home.html',{'name':context_processors.dict["name"]})
    else:
            print('home')
            return render(request,'home.html',{'name':'Guest '})


def signup(request):
    print('signup')
    print('denil signup')
    if request.method =='POST':
        print('going to signup')
        name=request.POST['orangeForm-Firstname']+'_'+request.POST['orangeForm-Lastname']
        
        email=request.POST['orangeFormemail']
        password=request.POST['orangeForm-pass']
        user = User.objects.create_user(username=name,email=email,password= password)
        user.save()
        print('singend in ')
    return render(request,'home.html',{'name':'home '})

def login(request):
    if request.method =='POST':
        username=request.POST['login-userid']
        password=request.POST['login-pass']
        
        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            context_processors.dict["testme"] = 'loggedin'
            context_processors.dict["name"] = username
            global globalUser
            globalUser=username
            return render(request,'dashboard.html',{'name':username})
        else:
            context_processors.dict["testme"] = 'notlogedin'
            print("if ->else user =",user)
            messages.info(request,'Invalid Credentials')
            return render(request,'home.html',{'name':'home '})
    else:
         context_processors.dict["testme"] = 'notlogedin'
        
         messages.info(request,'Invalid Credentials')        
         return render(request,'home.html',{'name':'Guest '})

def dashboard(request):
    return render(request,'dashboard.html',{'name':'home '})

def logout(request):
    print('logging out')
    auth.logout(request)
    context_processors.dict["testme"] = 'notlogedin'
    globalUser=""
    return redirect('/')
        

    

def productList(request):
    print('showing product List')
    list = [] 
    list=ProductList.objects.all()
    
    #list.append(newPro)
    #auth.logout(request)
    ##context_processors.dict["testme"] = 'notlogedin'
    return render(request,'productList.html',{'newPro':list,'current_username':globalUser})
        

def newProduct(request):
    print("going to add new product")
    product_name=request.POST['orangeForm-prod-name']
    product_price=request.POST['orangeForm-prod-price']
    product_available=request.POST['orangeForm-available-stock']
    product_desc=request.POST['orangeForm-prod-desc']
    product_image=request.POST['orangeForm-prod-image']
   
    product_user=globalUser
    print(product_name,'    ',
    product_price,'    ',
    product_available,'     ',
    product_desc,'    ',
    product_image,'  product_user   ',product_user)
    form=ProductList(product_name=product_name,product_desc=product_desc,product_rate=product_price,product_quantity=product_available,product_Img=product_image,product_user=product_user)
    #if form._isvalid(product_name,product_desc,product_price,product_available,product_image):
    if True:
      form.save()
      messages.info(request,'Product saved') 
      return render(request, 'productList.html',{'saved':'Product saved'})
    
   

def productDetail(request):
    print('show product details',request.path)
    currpath=request.path
    list_path=currpath.split('/')
    for i in range(len(list_path)-1):
        print(" list value",list_path[i+1],"    ")
    product_name=list_path[2]
    product_owner=list_path[3]
    
    return render(request,'productDetails.html',{'newPro':list,'current_username':globalUser})
        

    
