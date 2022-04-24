from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import product,category,User_Signup,Contact,Order,Company_Account,Service,Job,User_Contatact_Job,User_Contatact_Service,Ser_product,Ser_service,Ser_job,Ser_account,Ser_cat
from django.contrib.sessions.models import Session  
from django.contrib import messages
import stripe
import time
import json
import xlwt
from django.db.models import Q
from forex_python.converter import CurrencyRates,CurrencyCodes
import requests
# Create your views here.
stripe.api_key='sk_test_SD1VLYLcME6RYimXA3xxNKXW00eXfNnzuC'
# Create your views here.

def index(request):
    try:
        navdata=category.objects.all()
        allProds = product.objects.all().order_by('-pid')
        service1=Service.objects.filter(category="daily").order_by('-Service_id')
        service2=Service.objects.filter(category="monthly").order_by('-Service_id')
        service3=Service.objects.filter(category="yearly").order_by('-Service_id')
        job1=Job.objects.filter(category="highpaidjobs").order_by('-Job_id')
        job2=Job.objects.filter(category="recentjob").order_by('-Job_id')
        job3=Job.objects.filter(category="parttimejob").order_by('-Job_id')
        return render(request,'home.html',{'products':allProds,'navbar':navdata,'service1':service1,'service2':service2,'service3':service3,'job1':job1,'job2':job2,'job3':job3})
    except:
       
        return redirect('/')





def allproduct(request):
    if request.method == "POST":
        productname = request.POST.get('productname',False)
        location = request.POST.get('location',False)
      
        
        if productname and location:
            companydata = Company_Account.objects.filter(Company_Location__icontains = location)
            companyidList = []
            for i in companydata:
                companyidList.append(i.Company_Account_id)
        

            productdata = product.objects.filter(name__icontains = productname , Company_Account_Id__in = companyidList)
            navdata=category.objects.all()
            return render(request,'allproduct.html',{'product':productdata,'navbar':navdata})

        if productname:
            productdataname = product.objects.filter(name__icontains = productname)
            navdata=category.objects.all()
            return render(request,'allproduct.html',{'product':productdataname,'navbar':navdata})
            
        
        if location:
            companydata = Company_Account.objects.filter(Company_Location__icontains = location)
            companyidList = []
            for i in companydata:
                companyidList.append(i.Company_Account_id)
            

            productdatalocation = product.objects.filter(Company_Account_Id__in = companyidList)

          
            navdata=category.objects.all()
            return render(request,'allproduct.html',{'product':productdatalocation,'navbar':navdata})
      

    navdata=category.objects.all()
    allProds = product.objects.all().order_by('-pid')
    return render(request,'allproduct.html',{'product':allProds,'navbar':navdata})


###company location suggestion########

def locationsearch(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        companylocation = Company_Account.objects.filter(Company_Location__istartswith=q)[:5]
        results = []
        for location in companylocation:

            project_json = {}
            project_json['id'] = location.Company_Account_id
            project_json['value'] = location.Company_Location
            project_json['label'] = location.Company_Location
            results.append(project_json)
        print(results)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


###product name suggestion######

def productnamesearch(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        productname = product.objects.filter(name__istartswith=q)[:5]
        results = []
        for name in productname:

            project_json = {}
            project_json['id'] = name.pid
            project_json['value'] = name.name
            project_json['label'] = name.name
            results.append(project_json)
        print(results)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


####job name suggestion 

def jobnamesearch(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        jobname = Job.objects.filter(Job_Name__istartswith=q)[:5]
        results = []
        for name in jobname:

            project_json = {}
            project_json['id'] = name.Job_id
            project_json['value'] = name.Job_Name
            project_json['label'] = name.Job_Name
            results.append(project_json)
        print(results)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


####service name suggestion


def servicenamesearch(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        print(q)
        servicename = Service.objects.filter(Service_Name__istartswith=q)[:5]
        results = []
        for name in servicename:

            project_json = {}
            project_json['id'] = name.Service_id
            project_json['value'] = name.Service_Name
            project_json['label'] = name.Service_Name
            results.append(project_json)
        print(results)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)




###check suggestion

def suggestioncheck(request):
    return render(request,'suggestion.html')



#Product view
def products(request,myid):
    try:
        navdata=category.objects.all()
        products= product.objects.filter(pid=myid)
        return render(request,'productview.html',{'product':products,'navbar':navdata})
    except:
        return redirect('/')


# category list
def categories(request,cid):
    try:
        navdata=category.objects.all()
        products=product.objects.filter(category_id=cid)
        return render(request,'category.html',{'product':products,'navbar':navdata})
    except:
        return redirect('/')


# def cart(request):

#      if request.session.has_key('is_loged'):
#         cartcount=Cart.objects.filter(id= request.session['usercart'])[0]
#         request.session['counter']= cartcount.products.count()
#         cartsdata= Cart.objects.filter(id= request.session['usercart'])[0]
        
#         navdata=category.objects.all()
#         return render(request,'cart.html',{'cart':cartsdata,'navbar':navdata})
#      else:
#         return redirect('/')

# def updatecart(request , proid):

#     cart=Cart.objects.filter(id= request.session['usercart'])[0]
#     pro=product.objects.get(pid=proid)
#     if not pro in Cart.objects.filter(id= request.session['usercart']):
#         cart.products.add(pro)
    
#     new_cart= 0.00
#     for item in cart.products.all():
#         new_cart+= item.price
#     cart.total=float(new_cart)
#     cart.save()
#     return redirect('/cart')


# def removecart(request,cartid):
#     cart= Cart.objects.filter(id= request.session['usercart'])[0]
#     price= cart.products.get(pid=cartid)
#     newprice=cart.total
#     totalprice= newprice-price.price
#     cart.total=totalprice
#     cart.save()
#     cart.products.remove(cartid)
#     return redirect('/cart')

def checkout(request,id):
    
    if request.method=="POST":
        
        x=int(request.POST['totalamount'])
        api_key = '8DWA22DVZO227X94'
        from_c = 'USD'
        to_c = 'AED'
        base_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE'
        main_url = base_url + '&from_currency=' + from_c + '&to_currency=' + to_c + '&apikey=' + api_key
        response = requests.get(main_url)
        result = response.json()
        key = result['Realtime Currency Exchange Rate']
        rate = key['5. Exchange Rate']
       
    
        rate = float(rate)
        x = x / rate
       
        x = x*100
        x = int(x)
      
        
        
    
        charge = stripe.Charge.create(
        amount=x,
        currency='usd',
        description='A Django charge',
        source=request.POST['stripeToken']
        )

      
        if(charge['paid']==True):

            
            Firstname=request.POST['Firstname']
            lastname=request.POST['lastname']
            phoneno=request.POST['phoneno']
            emailid=request.POST['emailid']
            address=request.POST['address']
            city=request.POST['city']
            district=request.POST['district']
            zipcode=request.POST['zipcode']
            
            id=User_Signup.objects.get(sno=request.session['userid'])
           
            tokenid=request.POST['stripeToken']
            totalamount=request.POST['totalamount']
            Product_Quantity=request.POST['Product_Quantity']
            companyid=Company_Account.objects.get(Company_Account_id=request.POST['Company_Account'])
            productid=product.objects.get(pid=request.POST['productid'])
            orderdata=Order(Firstname=Firstname,lastname=lastname,phoneno=phoneno,emailid=emailid,address=address,city=city,district=district,zipcode=zipcode,User_Id=id,tokenid=tokenid,totalamount=totalamount,Product_Quantity=Product_Quantity,Company_Account_Id=companyid,Product_id=productid)
            
            orderdata.save()
            messages.success(request,"Item Payment Successfully")
            return redirect('/')
            



       
    try:
        UserAccount=User_Signup.objects.get(sno=request.session['userid'])
            
        quantity=request.GET['quantity']
        pquantity=float(quantity)
        productdata=product.objects.get(pid=id)

        pamount=productdata.price
        convert=float(pamount)
        producttotal=pquantity*convert
        finalamount=int(producttotal)
        
        navdata=category.objects.all() 
        return render(request,'checkout.html',{'navbar':navdata,'quantity':quantity,'data':productdata,'finalamount':finalamount,'quantity':quantity})


    except:
        
        messages.error(request,"Please Login first before checkout")
        return redirect('/login')
# Signup page
def signup(request):
    try:
        if request.method == 'POST':
            navdata=category.objects.all()
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            Whatsapp_No=request.POST['Whatsapp_No']
            Contact_No=request.POST['Contact_No']
            Location=request.POST['Location']
            password=request.POST['password']
            checkEmailRepeat = User_Signup.objects.filter(email = email)
            if checkEmailRepeat:
                messages.error(request,"Email Already Exist")
                return redirect('signup')
            checkcontact=User_Signup.objects.filter(Contact_No = Contact_No)
            if checkcontact:
                messages.error(request,"Contact Number Already Exist")
                return redirect('signup')
                
            data = User_Signup(fname=fname,lname=lname,email=email,password=password,Whatsapp_No=Whatsapp_No,Contact_No=Contact_No,Location=Location)
            data.save()
            messages.success(request,"Account Created Successfully")
            return redirect('login') 

            userdata=User_Signup.objects.get(email=email)
            myid=userdata.sno
        
            # mydata=Cart(user_id=myid)
            # mydata.save()
             
            
        navdata=category.objects.all() 
        return render(request,'signup.html',{'navbar':navdata})
    except:
        return redirect('/')

def login(request):
    # try:
    if request.method == 'POST':
            
        email=request.POST['email']
        password=request.POST['password']
        data = User_Signup.objects.get(Q(email = email) | Q(Contact_No = email))
      
        if data:
            if data.password == password:
                request.session['userid']=data.sno
                request.session['is_loged'] = True
                messages.success(request,"Login Successfully")
                return redirect('/')
            else:
                messages.error(request,"Password is Incorrect")
                return render(request,'login.html')
        
        else:
            messages.error(request,"your detail is wrong check your name or a password")
            return render(request,'login.html')

    
    navdata=category.objects.all()  
    return render(request,'login.html',{'navbar':navdata})
    # except:
    #     return redirect('/')

def logout(request):
    try:
        if request.session.has_key('is_loged'):

            del request.session['is_loged']
            # del request.session['counter']
            messages.success(request,"you are Sucessfully Logout")
            
            return redirect('/')

        else:
            
            messages.success(request,"you are Already logout")
            
            return render(request,'login.html')
    except:
        return redirect('/')

def contact(request):
    try:
        if request.method == 'POST':
            
            subject = request.POST['message']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            data = Contact(name=name,email=email,phone=phone,content=subject)
            data.save()
        
            messages.success(request,"Response Recorded Successfully")
            
            return render(request,'contact.html')
        navdata=category.objects.all()
        return render(request,'contact.html',{'navbar':navdata})
    except:
        return redirect('/')

def tracker(request):
    navdata=category.objects.all()
    return render(request,'tracking.html',{'navbar':navdata})


def charge(request):
    try:
        if request.method == 'POST':
            x=int(request.POST['amount'])
           
            
            
            charge = stripe.Charge.create(
            amount=x*100,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
            )

            if(charge['paid']==True):
                payment = transictions(tuser_id=request.session['id'],tprice=x,tamout=222,token=request.POST['stripeToken'],status_id_id=0)
                payment.save()

                return HttpResponse('source')
    except:
        return redirect('/')

def search(request):
    query = request.GET.get('search')
    
    data = product.objects.get(name__contains=query)
    
    navdata=category.objects.all()
    return render(request,'search.html',{'product':data,'navbar':navdata})

def serviceview(request,id):
    navdata=category.objects.all()
    singleservice= Service.objects.filter(Service_id=id)
    service= Service.objects.get(Service_id=id)
    # data=service.category
    # print(service)
    # singleservice=Service.objects.filter(category=data)
    # print(singleservice)
    navdata=category.objects.all()
    return render(request,'serviceview.html',{'service':service,'navbar':navdata,
    'singleservice':singleservice
    })

def allservices(request):
    if request.method == "POST":
        servicename = request.POST.get('service',False)
        location = request.POST.get('location',False)
      
      
        
        if servicename and location:
            companydata = Company_Account.objects.filter(Company_Location__icontains = location)
            companyidList = []
            for i in companydata:
                companyidList.append(i.Company_Account_id)
        

            servicedata = Service.objects.filter(Service_Name__icontains = servicename , Company_Account_Id__in = companyidList)

            navdata=category.objects.all()
            return render(request,'allservices.html',{'navbar':navdata,'allservice':servicedata})

        if servicename:
            
            servicedataname = Service.objects.filter(Service_Name__icontains = servicename)
            navdata=category.objects.all()
            return render(request,'allservices.html',{'navbar':navdata,'allservice': servicedataname})
            
        
        if location:
            companydata = Company_Account.objects.filter(Company_Location__icontains = location)
            companyidList = []
            for i in companydata:
                companyidList.append(i.Company_Account_id)

            servicedatalocation  = Service.objects.filter(Company_Account_Id__in = companyidList)
            navdata=category.objects.all()
            return render(request,'allservices.html',{'navbar':navdata,'allservice': servicedatalocation})

       
      
    
    try:
        allservice=Service.objects.all()
        navdata=category.objects.all()
        return render(request,'allservices.html',{'navbar':navdata,'allservice':allservice})
    except:
        return redirect('/')


def jobview(request,id):
    try:
        singlejob= Job.objects.filter(Job_id=id)
        # job= Job.objects.get(Job_id=id)
        # data=job.category
        # singlejob=Job.objects.filter(category=data)
        navdata=category.objects.all()
        return render(request,'jobview.html',{'navbar':navdata,'singlejob':singlejob})
    except:
        return redirect('/')

def alljob(request):
    if request.method == "POST":
        jobname = request.POST.get('job',False)
        location = request.POST.get('location',False)
      
      
        
        if jobname and location:
            companydata = Company_Account.objects.filter(Company_Location__contains = location)
            companyidList = []
            for i in companydata:
                companyidList.append(i.Company_Account_id)
        

            jobdata = Job.objects.filter(Job_Name__contains =  jobname,Company_Account_Id__in = companyidList)

            navdata=category.objects.all()
            return render(request,'alljob.html',{'navbar':navdata,'alljob': jobdata})
          

        if jobname:
            
            jobdataname = Job.objects.filter(Job_Name__contains =  jobname)
            navdata=category.objects.all()
            return render(request,'alljob.html',{'navbar':navdata,'alljob': jobdataname})
            
        
        if location:
            companydata = Company_Account.objects.filter(Company_Location__contains = location)
            companyidList = []
            for i in companydata:
                companyidList.append(i.Company_Account_id)

            jobdatalocation  = Job.objects.filter(Company_Account_Id__in = companyidList)
            navdata=category.objects.all()
            return render(request,'alljob.html',{'navbar':navdata,'alljob': jobdatalocation})

    alljob=Job.objects.all()
    navdata=category.objects.all()
    return render(request,'alljob.html',{'navbar':navdata,'alljob':alljob})

def servicecontact(request,id):
    
    
    try:
        if request.method == "POST":
            User_Id=request.session['userid']
            userid=User_Signup.objects.get(sno=User_Id)
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            password=request.POST['password']
            address=request.POST['address']
            city=request.POST['city']
            district=request.POST['district']
            phoneno=request.POST['phoneno']
            Whatsapp_No=request.POST['Whatsapp_No']
            Location=request.POST['Location']
            Desc=request.POST['Desc']
            servicedata=Service.objects.get(Service_id=id)
            companyid=servicedata.Company_Account_Id
            Service_id=Service.objects.get(Service_id=id)
            data=User_Contatact_Service(User_Id=userid,fname=fname,lname=lname,email=email,password=password,address=address,city=city,district=district,phoneno=phoneno,Whatsapp_No=Whatsapp_No,Location=Location,Desc=Desc,Comapnay_Id=companyid,Service_id=Service_id)
            data.save()
            messages.success(request,"Response Recorded Successfully")
            return redirect('/')


        id=Service.objects.get(Service_id=id)
        navdata=category.objects.all()
        return render(request,'servicecontact.html',{'navbar':navdata,'id':id})
    except:
        return redirect('/')

def jobcontact(request,id):
    try:
        if request.method == "POST":
            User_Id=request.session['userid']
            userid=User_Signup.objects.get(sno=User_Id)
            fname=request.POST['fname']
            lname=request.POST['lname']
            email=request.POST['email']
            password=request.POST['password']
            address=request.POST['address']
            city=request.POST['city']
            district=request.POST['district']
            phoneno=request.POST['phoneno']
            Whatsapp_No=request.POST['Whatsapp_No']
            Location=request.POST['Location']
            Desc=request.POST['Desc']
            jobdata=Job.objects.get(Job_id=id)
            companyid=jobdata.Company_Account_Id
            job_id=Job.objects.get(Job_id=id)
            data=User_Contatact_Job(User_Id=userid,fname=fname,lname=lname,email=email,password=password,address=address,city=city,district=district,phoneno=phoneno,Whatsapp_No=Whatsapp_No,Location=Location,Desc=Desc,Comapnay_Id=companyid,Job_id=job_id)
            data.save()
            messages.success(request,"Response Recorded Successfully")
            return redirect('/')
        
        id=Job.objects.get(Job_id=id)
        navdata=category.objects.all()
        return render(request,'jobcontact.html',{'navbar':navdata,'id':id})
    except:
        return redirect('/')


def serviceprovideraccount(request):
    if request.method == "POST":
        Company_Account_Name=request.POST['Company_Account_Name']
        Company_Account_Email=request.POST['Company_Account_Email']
        password=request.POST['password']
        Company_Account_logo=request.FILES['Company_Account_logo']
        Company_Account_Desc=request.POST['Company_Account_Desc']
        Contact=request.POST['Contact']
        Company_Adress=request.POST['Company_Adress']
        Company_Whatsapp_No=request.POST['Company_Whatsapp_No']
        Company_Location=request.POST['Company_Location']
        Service_Category=request.POST['Service_Category']
       
        checkEmailRepeat = Company_Account.objects.filter(Company_Account_Email = Company_Account_Email)
        if checkEmailRepeat:
            messages.error(request,"Email Already Exist")
            return redirect('serviceprovideraccount')
        
        data=Company_Account(Company_Account_Name=Company_Account_Name,Company_Account_Email=Company_Account_Email,password=password,Company_Account_logo=Company_Account_logo,Company_Account_Desc=Company_Account_Desc,Contact=Contact,Company_Adress=Company_Adress,Company_Whatsapp_No=Company_Whatsapp_No,Company_Location=Company_Location,Service_Category=Service_Category)
        data.save()
        messages.success(request,"Account Created Successfully")
        return redirect('serviceprovideraccount')
    navdata=category.objects.all()
    return render(request,'serviceprovider.html',{'navbar':navdata})

def serviceproviderlogin(request):
    if request.method == "POST":
        Company_Account_Email = request.POST['Company_Account_Email']
        password = request.POST['password']
        checkAuthenticate = Company_Account.objects.get(Company_Account_Email = Company_Account_Email)
        if checkAuthenticate:
            if checkAuthenticate.password == password:
                request.session['comapanyid'] = checkAuthenticate.Company_Account_id
                request.session['companyname'] = checkAuthenticate.Company_Account_Name
                return redirect('companyaccount')
    navdata=category.objects.all()
    return render(request,'serviceproviderlogin.html',{'navbar':navdata})

def companylogout(request):
    del request.session['comapanyid']
    del request.session['companyname']
    return redirect('/')


def Usercontact(request):
    data=Contact.objects.all().order_by('-sno')
    return render(request,'superadmin/contact.html',{'data':data})

def deletecontact(request):
    id = request.GET['id']
    data=Contact.objects.filter(sno=id)
    data.delete()
    messages.error(request,"Delete Sucessfully")
    return HttpResponse("Delete")

def companyaccount(request):
    data=Company_Account.objects.filter(Company_Account_id=request.session['comapanyid'])
    return render(request,'superadmin/companyaccount.html',{'data':data})

def editaccount(request):
    if request.method == "POST":
        
        
        Company_id=request.POST['Company_id']
        Company_Account_Name=request.POST['Company_Account_Name']
        password=request.POST['password']
        Company_Account_Desc=request.POST['Company_Account_Desc']
        Contact=request.POST['Contact']
        Company_Adress=request.POST['Company_Adress']
        Company_Whatsapp_No=request.POST['Company_Whatsapp_No']
        Company_Location=request.POST['Company_Location']
        getaccount = Company_Account.objects.get(Company_Account_id = Company_id)
        getaccount.Company_Account_Name = Company_Account_Name
        getaccount.password = password
        getaccount.Company_Account_Desc = Company_Account_Desc
        getaccount.Contact = Contact
        getaccount.Company_Adress = Company_Adress
        getaccount.Company_Whatsapp_No = Company_Whatsapp_No
        getaccount.Company_Location = Company_Location
        getaccount.save()
        

        
        messages.success(request,"Update Account Sucessfully")
        return redirect('/companyaccount')

    companyid = request.GET['id']
    userdata=list()
    subjectData = Company_Account.objects.get(Company_Account_id = companyid )
    mydata=(Ser_account(subjectData))
    userdata.append(mydata.data)
    return HttpResponse(json.dumps(userdata))



def contactjobs(request):
    data=User_Contatact_Job.objects.filter(Comapnay_Id=request.session['comapanyid']).order_by('-User_Contatact_Job_id')
    return render(request,'superadmin/contactjobs.html',{'data':data})

def deletejobs(request):
    id = request.GET['id']
    data=User_Contatact_Job.objects.filter(User_Contatact_Job_id=id)
    data.delete()
    messages.error(request,"Delete Sucessfully")
    return HttpResponse("Delete")



def contactservices(request):
    data=User_Contatact_Service.objects.filter(User_Contatact_Service_id=request.session['comapanyid']).order_by('-User_Contatact_Service_id')
    return render(request,'superadmin/contactservices.html',{'data':data})

def deleteservices(request):
    id = request.GET['id']
    data=User_Contatact_Service.objects.filter(User_Contatact_Service_id=id)
    data.delete()
    messages.error(request,"Delete Sucessfully")
    return HttpResponse("Delete")



def productorder(request):
    id=request.session['comapanyid']
    data=Order.objects.filter(Company_Account_Id=id).order_by('-order_id')
    return render(request,'superadmin/productorder.html',{'data':data})

def deleteproductorder(request):
    id = request.GET['id']
    data=Order.objects.filter(order_id=id)
    data.delete()
    messages.error(request,"Delete Sucessfully")
    return HttpResponse("Delete")



def productcategory(request):
    id=request.session['comapanyid']
    data=category.objects.filter(Company_Account_Id=id).order_by('-cid')
    return render(request,'superadmin/productcategory.html',{'data':data})

def deleteproductcategory(request):
    id = request.GET['id']
    data=category.objects.filter(cid=id)
    data.delete()
    messages.error(request,"Delete Sucessfully")
    return HttpResponse("Delete")

def addproductcategory(request):
    if request.method == "POST":
        cname=request.POST['cname']
        id=request.session['comapanyid']
        
        companyid=Company_Account.objects.get(Company_Account_id=id)
        checkAuthenticate=category.objects.filter(cname = cname,Company_Account_Id=id)
        if checkAuthenticate:
            messages.error(request,"Category Already Exist")
            return redirect('productcategory')
        else:
            data=category(cname=cname,Company_Account_Id=companyid)
            data.save()
            messages.success(request,"Category Added Successfully")
            return redirect('productcategory')

    return render(request,'superadmin/productcategory.html')


def editproductcategory(request):
    if request.method == "POST":
        id=request.session['comapanyid']
        cid=request.POST['cid']
        cname=request.POST['cname']
        checkAuthenticate=category.objects.filter(cname = cname,Company_Account_Id=id)
        if checkAuthenticate:
            messages.error(request,"Category Already Exist")
            return redirect('productcategory')
        else:
            getaccount = category.objects.get(cid = cid)
            getaccount.cname = cname
            getaccount.save()
            messages.success(request,"Update Category Sucessfully")
            return redirect('/productcategory')
        
        
    cid = request.GET['id']
    userdata=list()
    catData = category.objects.get(cid = cid )
    mydata=(Ser_cat(catData))
    userdata.append(mydata.data)
    return HttpResponse(json.dumps(userdata))





































































































































































#admin work 

##############Admin#############
def serviceprovider(request):
    if not request.session.has_key('comapanyid'):
        return redirect('/')

    
    companydata = Company_Account.objects.get(Company_Account_id=request.session['comapanyid'])
    data=companydata.Service_Category
    request.session['company'] = data
    return render(request,'superadmin/companyaccount.html')
    
    

  
    


# add and show product
def adminproducts(request):
    if request.method == "POST":
        image = request.FILES['product_Image']
        title  = request.POST['title']
        offer  = request.POST['offer']
        productcategory = request.POST['category']
        price = request.POST['price']
        stock = request.POST['stock']
        desc = request.POST['desc']
        company_id = Company_Account.objects.get(Company_Account_id = request.session['comapanyid'] )
        categoryobject = category.objects.get(cid = productcategory )

        data = product(name = title,category =  categoryobject ,price = price,stock = stock,description = desc,image = image , Product_offers = offer,Company_Account_Id = company_id)
        data.save()

        messages.success(request,"Added Sucessfully")
        return redirect('/adminproducts')

        
    
        

    categoryData = category.objects.all()
    productData = product.objects.filter(Company_Account_Id = request.session['comapanyid']).order_by('-pid')
    return render(request,'superadmin/products.html',{'categorydata':categoryData,'product':productData})

#delete product

def deleteproducts(request,id):
    productData = product.objects.get(pid = id)
    productData.delete()
    messages.success(request,"Delete Sucessfully")
    return redirect('/adminproducts')

#edit product

def edit_product(request):
    if request.method == "POST":
        image = request.FILES.get('product_Image',False)
        title  = request.POST['title']
        offer  = request.POST['offer']
        productcategory = request.POST['category']
        price = request.POST['price']
        stock = request.POST['stock']
        desc = request.POST['desc']
        productId = request.POST['productid']

        editproduct = product.objects.get(pid = productId)
        editproduct.name = title
        editproduct. category = category.objects.get(cid = productcategory)
        editproduct.price = price
        editproduct.stock = stock
        editproduct.description = desc
        editproduct.Product_offers = offer
        editproduct.save()

        if image:
            editproduct.image = image
            editproduct.save()
          
        messages.success(request,"Update Sucessfully")
        return redirect('/adminproducts')
    userdata=list()
    productid = request.GET['id']
    productdata = product.objects.get(pid = productid)
    mydata=Ser_product(productdata)
    userdata.append(mydata.data)
    return HttpResponse(json.dumps(userdata))
    




  




##show and add job

def jobs(request):
    if request.method == "POST":
        image = request.FILES['image']
        jobname = request.POST['jobname']
        exp = request.POST['Experience']
        email = request.POST['email']
        contact = request.POST['contact']
        category = request.POST['Category_Id']
        Decsription = request.POST['Decsription']
        company_id = Company_Account.objects.get(Company_Account_id = request.session['comapanyid'] )

        data = Job(Job_Name = jobname,Job_Description = Decsription,Job_Image = image,Experience_Required = exp,Email = email,Contact = contact,category = category,Company_Account_Id = company_id )
        data.save()
        messages.success(request,"Added Sucessfully")
        return redirect('/jobs')




    jobdata = Job.objects.filter(Company_Account_Id =  request.session['comapanyid'] ).order_by('-Job_id')
    return render(request,'superadmin/jobs.html',{'job':jobdata})

##edit job

def edit_job(request):
    if request.method == 'POST':
        image = request.FILES.get('image',False)
        jobname = request.POST['jobname']
        exp = request.POST['Experience']
        email = request.POST['email']
        contact = request.POST['contact']
        category = request.POST['Category_Id']
        Decsription = request.POST['Decsription']
        jobId = request.POST['jobid']

        jobdata = Job.objects.get( Job_id =  jobId )
        jobdata.Job_Name = jobname
        jobdata.Job_Description = Decsription
        jobdata.Experience_Required = exp
        jobdata.Email = email
        jobdata.Contact = contact
        jobdata.category = category
        jobdata.save()

        if image:
            jobdata.Job_Image = image
            jobdata.save()

        messages.success(request,"Edit Sucessfully")
        return redirect('/jobs')


        

    userdata=list()
    jobid = request.GET['id']
    jobdata = Job.objects.get( Job_id =  jobid )
    mydata=Ser_job(jobdata)
    userdata.append(mydata.data)
    return HttpResponse(json.dumps(userdata))
   


   
    


###delete job

def deletejob(request,id):
    jobdata = Job.objects.get(Job_id = id )
    jobdata.delete()
    messages.success(request,"Delete Sucessfully")
    return redirect('/jobs')


#show and add service

def services(request):
    if request.method == "POST":
        image = request.FILES['image']
        servicename = request.POST['Sname']
        email = request.POST['email']
        contact = request.POST['contact']
        servicecategory = request.POST['category']
        servicedes = request.POST['desc']
        company_id = Company_Account.objects.get(Company_Account_id = request.session['comapanyid'] )

        data = Service(Service_Name = servicename, Service_Description = servicedes,Service_Image = image, Email = email,Contact = contact,category = servicecategory,Company_Account_Id = company_id)
        data.save()
        messages.success(request,"Added Sucessfully")
        return redirect('/services')
        
        



    showservice = Service.objects.filter(Company_Account_Id = request.session['comapanyid'] ).order_by('-Service_id')
    return render(request,'superadmin/services.html',{'service':showservice})


#delete service

def deleteservice(request,id):
    servicedata = Service.objects.get(Service_id = id)
    servicedata.delete()
    messages.success(request,"Delete Sucessfully")
    return redirect('/services')



##edit service

def edit_service(request):
    if request.method == "POST":
        image = request.FILES.get('image',False)
        servicename = request.POST['Sname']
        email = request.POST['email']
        contact = request.POST['contact']
        servicecategory = request.POST['category']
        servicedesc = request.POST['desc']
        serId = request.POST['serviceid']

        Serdata = Service.objects.get(Service_id = serId)
        Serdata.Service_Name = servicename
        Serdata.Service_Description = servicedesc
        Serdata.Service_Email = email
        Serdata.Contact= contact
        Serdata.category= servicecategory
        Serdata.save()

        if image:
            Serdata.Service_Image = image
            Serdata.save()

        messages.success(request,"Update Sucessfully")
        return redirect('/services')

        


       

    userdata=list()
    service_id = request.GET['id']
    servicedata = Service.objects.get(Service_id = service_id)
    mydata=Ser_service(servicedata)
    userdata.append(mydata.data)
    return HttpResponse(json.dumps(userdata))



def carts(request):
    return render(request,'superadmin/carts.html')

def servicecategory(request):
    return render(request,'superadmin/servicecategory.html')


def exportproducts(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Orders.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    # columns = ['Product Image', 'Product Name', 'Product Quantity', 'Username','First Name','Last Name','Email','Address','City','District','Location','Zipcode','Phone Number','Whatsapp Number','Total Amount','Status','Order Date Time' ]
    columns = ['Product_Quantity','First_Name','Last_Name','Email','Address','City','District','Zipcode','Phone_Number','Total_Amount','Status' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    # rows = Order.objects.all().values_list('Product_id.image', 'Product_id.name', 'Product_Quantity', 'User_Id.fname','User_Id.lname','emailid','address','city','district','User_Id.Location','phoneno','User_Id.Whatsapp_No','totalamount','status','timestamp')
    rows = Order.objects.all().values_list('Product_Quantity','Firstname','lastname','emailid','address','city','district','zipcode','phoneno','totalamount','status')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def exportservice(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Service Image', 'Service Name','Username','First Name','Last Name','Email','Address','City','District','Location','Phone Number','Whatsapp Number','Desc']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User_Contatact_Service.objects.all().values_list('U_Fname', 'U_Lname', 'U_Email', 'Username','SPassword','U_ContactNo','U_Desc','Gender','DOB','Joining_Date','Status','Subscription')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response




def exportjob(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Job Image', 'Job Name','Username','First Name','Last Name','Email','Address','City','District','Location','Phone Number','Whatsapp Number','Desc']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = User_Contatact_Job.objects.all().values_list('U_Fname', 'U_Lname', 'U_Email', 'Username','SPassword','U_ContactNo','U_Desc','Gender','DOB','Joining_Date','Status','Subscription')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


def checking(request):
    data = Order.objects.all()
    cartlist = []
    for i in data:
        cartlist.append(i.cart)

    productlist = []
    for j in cartlist:
        productlist.append(j.products)


    return HttpResponse(productlist)

def userforget(request):
    if request.method=="POST":
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            try:
                check=User_Signup.objects.get(email=email)
                if check:
                    check.email=email
                    check.password=password1
                    check.save()
                    messages.success(request,"Password Updated Successfully")
                    return redirect('/login')
                else:
                    messages.success(request,"Incorrect Email")
                    return redirect('/userforget')
            except:
                messages.success(request,"Incorrect Email")
                return redirect('/userforget')

                
        else:

            messages.success(request,"Password Does Not Match")
            return redirect('/userforget')
            



        



    navdata=category.objects.all()
    return render(request,'userforget.html',{'navbar':navdata})

def companyforget(request):
    if request.method=="POST":
        Company_Account_Email=request.POST['Company_Account_Email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2:
            try:
                check=Company_Account.objects.get(Company_Account_Email=Company_Account_Email)
                if check:
                    check.Company_Account_Email=Company_Account_Email
                    check.password=password1
                    check.save()
                    messages.success(request,"Password Updated Successfully")
                    return redirect('/serviceproviderlogin')
                else:
                    messages.error(request,"Incorrect Email")
                    return redirect('/companyforget')
            except:
                messages.error(request,"Incorrect Email")
                return redirect('/companyforget')

                
        else:

            messages.success(request,"Password Does Not Match")
            return redirect('/userforget')
    navdata=category.objects.all()
    return render(request,'companyforget.html',{'navbar':navdata})