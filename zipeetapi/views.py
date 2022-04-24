from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser
import requests
import json
import stripe
from django.db.models import Q
from app.models import product,category,User_Signup,Contact,Order,Company_Account,Service,Job,User_Contatact_Job,User_Contatact_Service,Ser_product,Ser_service,Ser_job,Ser_account,Ser_cat,Ser_Signup,Ser_Order
from zipeetapi.serializers import SerCompany_Account,DynamicSerCompany_Account
#secrete key
stripe.api_key='sk_test_QhSeKSq3sLTxE0VIwmsh1K9o00cU4DXYYq'
from forex_python.converter import CurrencyRates,CurrencyCodes


class navBarData(APIView):
  def get(self,request):

    try:
      
      
      navdata=category.objects.all()
      
      
      

      category_Data =(Ser_cat(navdata,many=True))
      message = {
        'status' : True,
        'category_Data' : category_Data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class Products(APIView):

  def get(self,request):

    try:

      allProds = product.objects.all().order_by('-pid')
      product_data = Ser_product(allProds,many=True)

      message = {
        'status' : True,
        'product_data' : product_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class dailyService(APIView):

  def get(self,request):

    try:

      Daily_service=Service.objects.filter(category="daily").order_by('-Service_id')
      service_data = Ser_service(Daily_service,many=True)

      message = {
        'status' : True,
        'service_data' : service_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class monthlyService(APIView):

  def get(self,request):

    try:

      Monthly_service=Service.objects.filter(category="monthly").order_by('-Service_id')
      service_data = Ser_service(Monthly_service,many=True)

      message = {
        'status' : True,
        'service_data' : service_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class yearlyService(APIView):

  def get(self,request):

    try:

      Yearly_service=Service.objects.filter(category="yearly").order_by('-Service_id')
      service_data = Ser_service(Yearly_service,many=True)

      message = {
        'status' : True,
        'service_data' : service_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)


class highpaidJobs(APIView):

  def get(self,request):

    try:

      High_Paid_Jobs=Job.objects.filter(category="highpaidjobs").order_by('-Job_id')
      job_data = Ser_job(High_Paid_Jobs,many=True)

      message = {
        'status' : True,
        'job_data' : job_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)




class recentJobs(APIView):

  def get(self,request):

    try:

      Recent_Jobs=Job.objects.filter(category="recentjob").order_by('-Job_id')
      job_data = Ser_job(Recent_Jobs,many=True)

      message = {
        'status' : True,
        'job_data' : job_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)


     


class parttimeJobs(APIView):

  def get(self,request):

    try:

      PartTime_Jobs=Job.objects.filter(category="parttimejob").order_by('-Job_id')
      job_data = Ser_job(PartTime_Jobs,many=True)

      message = {
        'status' : True,
        'job_data' : job_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)




class Show_All_Products(APIView):


  def get(self,request):

    try:

      allProds = product.objects.all().order_by('-pid')
      product_data = Ser_product(allProds,many=True)

      message = {
        'status' : True,
        'product_data' : product_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)


class Show_All_Services(APIView):


  def get(self,request):

    try:

      allService = Service.objects.all().order_by('-Service_id')
      service_data = Ser_service(allService,many=True)

      message = {
        'status' : True,
        'service_data' : service_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class Show_All_Jobs(APIView):


  def get(self,request):

    try:

      allJob = Job.objects.all().order_by('-Job_id')
      job_data = Ser_job(allJob,many=True)

      message = {
        'status' : True,
        'job_data' : job_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class View_Product(APIView):

  def get(self,request):

    try:

      pid = request.GET['pid']

      products= product.objects.filter(pid=pid)
      product_data = Ser_product(products,many=True)

      message = {
        'status' : True,
        'product_data' : product_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)


class View_Service(APIView):

  def get(self,request):

    try:

      sid = request.GET['sid']

      services= Service.objects.filter(Service_id=sid)
      service_data = Ser_service(services,many=True)

      message = {
        'status' : True,
        'service_data' : service_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class View_Job(APIView):

  def get(self,request):

    try:

      jid = request.GET['jid']

      jobs= Job.objects.filter(Job_id=jid)
      job_data = Ser_job(jobs,many=True)

      message = {
        'status' : True,
        'job_data' : job_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)


class View_Category_Data(APIView):


  def get(self,request):

    try:

  
      cid=request.GET['cid']

      products=product.objects.filter(category_id=cid)
      category_data = Ser_product(products,many=True)

      message = {
        'status' : True,
        'category_data' : category_data.data
            }
                  
      return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)




class Customer_Contact(APIView):

  def post(self,request):

    try:

      subject = request.data.get('message')
      name = request.data.get('name')
      email = request.data.get('email')
      phone = request.data.get('phone')
      data = Contact(name=name,email=email,phone=phone,content=subject)
      data.save()

      message = {

                'status' : True,
                'message' : "Response Record SuccessFully"
            }
      return Response(message)


    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)








class User_signUp(APIView):

  def post(self,request):

    try:

      fname=request.data.get('fname')
      lname=request.data.get('lname')
      email=request.data.get('email')
      Whatsapp_No=request.data.get('Whatsapp_No')
      Contact_No=request.data.get('Contact_No')
      Location=request.data.get('Location')
      password=request.data.get('password')
      checkEmailRepeat = User_Signup.objects.filter(email = email)
      if checkEmailRepeat:
        message = {

                  'status' : False,
                  'message' : "Email Already Exist"
              }
        return Response(message)


          
      checkcontact=User_Signup.objects.filter(Contact_No = Contact_No)
      if checkcontact:
        message = {

                  'status' : False,
                  'message' : "Contact Number Already Exist"
              }
        return Response(message)

      else:
         
          
        data = User_Signup(fname=fname,lname=lname,email=email,password=password,Whatsapp_No=Whatsapp_No,Contact_No=Contact_No,Location=Location)
        data.save()

        message = {

                    'status' : True,
                    'message' : "Signup SuccessFully"
                }
        return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class User_Login(APIView):

  def post(self,request):


    try:

      email=request.data.get('email')
      password=request.data.get('password')
      data = User_Signup.objects.filter(Q(email = email) | Q(Contact_No = email))
    
      if data:

          data = data[0]
          if data.password == password:
              request.session['userid']=data.sno
              request.session['is_loged'] = True

              order_data = Order.objects.filter(User_Id = request.session['userid'])
              if data:

                order_count = order_data.count()
                serializers = Ser_Signup(data)
               
                message = {

                      'status' : True,
                      'message' : "Login SuccessFully",
                      'data':serializers.data,
                      'order_count':order_count
                  }
                return Response(message)
          else:
              
              message = {

                  'status' : False,
                  'message' : "Password or Email Incorrect"
              }
              return Response(message)
      
      else:
          message = {

                  'status' : False,
                  'message' : "Password or Email Incorrect"
              }
          return Response(message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)




class Checkout(APIView):

  def get(self,request):

    try:

      userid = request.GET['user_id']
      pid = request.GET['pid']
      quantity=request.GET['quantity']

      UserAccount=User_Signup.objects.get(sno=userid)
      pquantity=float(quantity)
      productdata=product.objects.get(pid=pid)
      product_data = Ser_product(productdata)


      pamount=productdata.price
    
      convert=float(pamount)
      producttotal=pquantity*convert
      finalamount=int(producttotal)

    

      message = {

                  'status' : True,
                  'quantity':quantity,
                  'finalamount':finalamount,
                  'data':product_data.data,
                  
                  
              }
      return Response(message)


    except Exception as e:

            
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)
        
  
  def post(self,request):

    try:

      x=int(request.data.get('totalamount'))
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

      Card_number=request.data.get('Card_number')
      Cvc=request.data.get('Cvc')
      expiration_date=request.data.get('expiration_date')
      cvc = request.data.get('cvc')
      year=expiration_date[0:4]
      month=expiration_date[5:7]

      try:
        createtoken = stripe.Token.create(
        card={
        "number": Card_number,
        "exp_month": month,
        "exp_year":year ,
        "cvc": Cvc,
        },
        )
            
        
       
        charge = stripe.Charge.create(
        amount = x,
        currency='usd',
        description='Apointment created',
        source = createtoken
        )

      except stripe.error.CardError as e:

        Message={
                'status' : False,
                'message': str(e)
            }
        return Response(Message)

      if(charge['paid']==True):

          
        Firstname=request.data.get('Firstname')
        lastname=request.data.get('lastname')
        phoneno=request.data.get('phoneno')
        emailid=request.data.get('emailid')
        address=request.data.get('address')
        city=request.data.get('city')
        district=request.data.get('district')
        zipcode=request.data.get('zipcode')
        userid = request.data.get('user_id')
        
        id=User_Signup.objects.get(sno=userid)
       
        
        totalamount=request.data.get('totalamount')
        Product_Quantity=request.data.get('Product_Quantity')
        companyid=Company_Account.objects.get(Company_Account_id=request.data.get('Company_Account'))
        productid=product.objects.get(pid=request.data.get('productid'))

        orderdata=Order(Firstname=Firstname,lastname=lastname,phoneno=phoneno,emailid=emailid,address=address,city=city,district=district,zipcode=zipcode,User_Id=id,totalamount=totalamount,Product_Quantity=Product_Quantity,Company_Account_Id=companyid,Product_id=productid)
        
        orderdata.save()
        
        message = {

                  'status' : True,
                  'message' : "Item Payment Successfully"
              }
        return Response(message)

    except Exception as e:
            
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)



            
            


class Products_Search(APIView):

  def post(self,request):


    try:


      productname = request.data.get('productname',False)
      location = request.data.get('location',False)
    
      
      if productname and location:
          companydata = Company_Account.objects.filter(Company_Location__icontains = location)
          companyidList = []
          for i in companydata:
              companyidList.append(i.Company_Account_id)
      

          productdata = product.objects.filter(name__icontains = productname , Company_Account_Id__in = companyidList)

          product_Data = Ser_product(productdata,many=True)
          
          Message={
                  'status' : True,
                  'product_Data': product_Data.data,
                 


                  }
          return Response(Message)

      if productname:
          productdataname = product.objects.filter(name__icontains = productname)
          
          product_Data = Ser_product(productdataname,many=True)
          
          Message={
                  'status' : True,
                  'product_Data': product_Data.data,
                 


                  }
          return Response(Message)
          
      
      if location:
          companydata = Company_Account.objects.filter(Company_Location__icontains = location)
          companyidList = []
          for i in companydata:
              companyidList.append(i.Company_Account_id)
          

          productdatalocation = product.objects.filter(Company_Account_Id__in = companyidList)

        
          product_Data = Ser_product(productdatalocation,many=True)
          
          Message={
                  'status' : True,
                  'product_Data': product_Data.data,
                 


                  }
          return Response(Message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)




class Job_Search(APIView):

  def post(self,request):


    try:


      jobname = request.data.get('jobname',False)
      location = request.data.get('location',False)
    
      
      if jobname and location:
          companydata = Company_Account.objects.filter(Company_Location__icontains = location)
          companyidList = []
          for i in companydata:
              companyidList.append(i.Company_Account_id)
      

          jobdata = Job.objects.filter(Job_Name__icontains = jobname , Company_Account_Id__in = companyidList)

          job_Data = Ser_job(jobdata,many=True)
          
          Message={
                  'status' : True,
                  'job_Data': job_Data.data,
                


                  }
          return Response(Message)

      if jobname:
          jobdata = Job.objects.filter(Job_Name__icontains = jobname)
          
          job_Data = Ser_job(jobdata,many=True)
          
          Message={
                  'status' : True,
                  'job_Data': job_Data.data,
                


                  }
          return Response(Message)
          
      
      if location:
          companydata = Company_Account.objects.filter(Company_Location__icontains = location)
          companyidList = []
          for i in companydata:
              companyidList.append(i.Company_Account_id)
          

          jobdata = Job.objects.filter(Company_Account_Id__in = companyidList)

        
          
          
          job_Data = Ser_job(jobdata,many=True)
          
          Message={
                  'status' : True,
                  'job_Data': job_Data.data,
                


                  }
          return Response(Message)

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



class Service_Search(APIView):

  def post(self,request):

    try:


      servicename = request.data.get('servicename',False)
      location = request.data.get('location',False)
    
      
      if servicename and location:
          companydata = Company_Account.objects.filter(Company_Location__icontains = location)
          companyidList = []
          for i in companydata:
              companyidList.append(i.Company_Account_id)
      

          servicedata = Service.objects.filter(Service_Name__icontains = servicename , Company_Account_Id__in = companyidList)

          service_Data = Ser_service(servicedata,many=True)
          
          Message={
                  'status' : True,
                  'service_Data': service_Data.data,
                


                  }
          return Response(Message)

      if servicename:
          servicedata = Service.objects.filter(Service_Name__icontains = servicename)
          
          service_Data = Ser_service(servicedata,many=True)
          
          Message={
                  'status' : True,
                  'service_Data': service_Data.data,
                


                  }
          return Response(Message)
          
      
      if location:
          companydata = Company_Account.objects.filter(Company_Location__icontains = location)
          companyidList = []
          for i in companydata:
              companyidList.append(i.Company_Account_id)
          

          servicedata = Service.objects.filter(Company_Account_Id__in = companyidList)

        
          
          
          service_Data = Ser_service(servicedata,many=True)
          
          Message={
                  'status' : True,
                  'service_Data': service_Data.data,
                


                  }
          return Response(Message)


    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)


class servicecontact(APIView):

  def post(self,request):

      
      
    try:
        
        User_Id=request.POST['userid']
        Service_id=request.POST['Service_id']
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
        servicedata=Service.objects.get(Service_id=Service_id)
        companyid=servicedata.Company_Account_Id
        Service_id=Service.objects.get(Service_id=Service_id)
        data=User_Contatact_Service(User_Id=userid,fname=fname,lname=lname,email=email,password=password,address=address,city=city,district=district,phoneno=phoneno,Whatsapp_No=Whatsapp_No,Location=Location,Desc=Desc,Comapnay_Id=companyid,Service_id=Service_id)
        data.save()
        Message={
                'status' : True,
                'message': "Response Recorded Successfully"
              


                }
        return Response(Message)

        


    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


class jobcontact(APIView):

  def post(self,request):

      
      
    try:
        
        User_Id=request.POST['userid']
        Job_id=request.POST['Job_id']
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
        jobdata=Job.objects.get(Job_id=Job_id)
        companyid=jobdata.Company_Account_Id
        job_id=Job.objects.get(Job_id=Job_id)
        data=User_Contatact_Job(User_Id=userid,fname=fname,lname=lname,email=email,password=password,address=address,city=city,district=district,phoneno=phoneno,Whatsapp_No=Whatsapp_No,Location=Location,Desc=Desc,Comapnay_Id=companyid,Job_id=job_id)
        data.save()
        Message={
                'status' : True,
                'message': "Response Recorded Successfully"
              


                }
        return Response(Message)

        


    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)










  #########################    SHakeeb APi ###############################


    ##signup company account
class companyAccountSignup(APIView):

  def post(self,request):

    try:
      Company_Account_Name=request.POST['Company_Account_Name']
      Company_Account_Email=request.POST['Company_Account_Email']
      password=request.POST['password']
      # Company_Account_logo=request.FILES['Company_Account_logo']
      Company_Account_Desc=request.POST['Company_Account_Desc']
      Contact=request.POST['Contact']
      Company_Adress=request.POST['Company_Adress']
      Company_Whatsapp_No=request.POST['Company_Whatsapp_No']
      Company_Location=request.POST['Company_Location']
      Service_Category=request.POST['Service_Category']
      
      checkEmailRepeat = Company_Account.objects.filter(Company_Account_Email = Company_Account_Email)
      if checkEmailRepeat:
        message = {
          'status' : False,
          'message' : "Account Already Exist"
        }
        return Response(message)


      else:
        data=Company_Account(Company_Account_Name=Company_Account_Name,Company_Account_Email=Company_Account_Email,password=password,Company_Account_Desc=Company_Account_Desc,Contact=Contact,Company_Adress=Company_Adress,Company_Whatsapp_No=Company_Whatsapp_No,Company_Location=Company_Location,Service_Category=Service_Category)
        data.save()
        message = {
          'status' : True,
          'message' : "Account Create Successfully"
        }
        return Response(message)
    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


##Login company account

class companyAccountLogin(APIView):
  def post(self,request):

    try:
      Company_Account_Email = request.POST['Company_Account_Email']
      password = request.POST['password']
      checkAuthenticate = Company_Account.objects.get(Company_Account_Email = Company_Account_Email)
      if checkAuthenticate:
          if checkAuthenticate.password == password:
            companyAccountObject = DynamicSerCompany_Account(checkAuthenticate)
            message = {
              'status' : True,
              'message' : "Login Successfully",
              'data' : companyAccountObject.data
            }
            return Response(message)

          else:
            message = {
              'status' : False,
              'message' : "Invalide Credential"
            }
            return Response(message)
    except:
      message = {
      'status' : False,
      'message' : "Invalide Credential"
      }
      return Response(message)


#AddProductCategory
class AddProductCategory(APIView):
  def post(self,request):

    try:
      cname=request.POST['categoryname']
      id=request.POST['comapanyid']
      
      companyid=Company_Account.objects.get(Company_Account_id=id)
      checkAuthenticate=category.objects.filter(cname = cname,Company_Account_Id=id)
      if checkAuthenticate:
        message = {
        'status' : False,
        'message' : "Category Already Exist"
        }
        return Response(message)

         
      else:
          data=category(cname=cname,Company_Account_Id=companyid)
          data.save()
          message = {
            'status' : True,
            'message' : "Category Add Successfully"
          }
          return Response(message)
    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)
        

##showProductCategory

class showProductCategory(APIView):
  def get(self,request):

    try:

      id=request.GET['comapanyid']
      categorydata = category.objects.filter(Company_Account_Id=id)
      serCategory = Ser_cat(categorydata,many=True)
      message = {
            'status' : True,
            'data' : serCategory.data
          
          }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


##Delete Category
class deleteCategory(APIView):
   def get(self,request):
    id=request.GET['categoryid']
    categorydata = category.objects.get(cid=id)
    categorydata.delete()
    
    message = {
          'status' : True,
          'message': "Delete Successfully"
    
        
        }
    return Response(message)


###AddProducts and show 

class AddProducts(APIView):

  def post(self,request):

    try:

      image = request.FILES['product_Image']
      title  = request.POST['title']
      offer  = request.POST['offer']
      productcategory = request.POST['categoryid']
      price = request.POST['price']
      stock = request.POST['stock']
      desc = request.POST['desc']
      id = request.POST['comapanyid']
      company_id = Company_Account.objects.get(Company_Account_id = id )
      categoryobject = category.objects.get(cid = productcategory )

      data = product(name = title,category =  categoryobject ,price = price,stock = stock,description = desc,image = image , Product_offers = offer,Company_Account_Id = company_id)
      data.save()

      message = {
            'status' : True,
            'message': "Add Product Successfully"
      
          
          }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)

  def get(self,request):

    try:

      id = request.GET['comapanyid']
      productData = product.objects.filter(Company_Account_Id = id).order_by('-pid')
      if productData:
        serProduct = Ser_product(productData,many=True)
        message = {
        'status' : True,
        'data' : serProduct.data
            
        
            
            }
        return Response(message)

      else:
        message = {
          'status' : False,
          'message' : "No Products is Available"
            
        
            
            }
        return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


##Delete Product 
class DeleteProduct(APIView):

  def get(self,request):

    try:

      id = request.GET['productId']
      productData = product.objects.get(pid = id)
      productData.delete()
      message = {
          'status' : True,
          'message' : "Delete Successfully"
            
        
            
            }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


##Add jobs and show
class AddJobs(APIView):
  def post(self,request):

    try:



      image = request.FILES['image']
      jobname = request.POST['jobname']
      exp = request.POST['Experience']
      email = request.POST['email']
      contact = request.POST['contact']
      category = request.POST['category']
      Decsription = request.POST['Decsription']
      id = request.POST['comapanyid']
      company_id = Company_Account.objects.get(Company_Account_id = id )

      data = Job(Job_Name = jobname,Job_Description = Decsription,Job_Image = image,Experience_Required = exp,Email = email,Contact = contact,category = category,Company_Account_Id = company_id )
      data.save()
      message = {
        'status' : True,
        'message' : "Job Post Successfully"
          
      
          
          }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)



  def get(self,request):

    try:

      id = request.GET['comapanyid']
      jobdata = Job.objects.filter(Company_Account_Id = id ).order_by('-Job_id')
      if jobdata:
        serjob = Ser_job(jobdata,many=True)
        message = {
          'status' : True,
          'data' : serjob.data
            
        
            
            }
        return Response(message)

      else:
        message = {
        'status' : False,
        'message' : "No Jobs is Available"
          
      
          
          }
        return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)




##Delete job 
class DeleteJob(APIView):
  def get(self,request):

    try:

      id = request.GET['jobid']
      jobdata = Job.objects.get(Job_id = id )
      jobdata.delete()
      message = {
        'status' : True,
        'message' : "Delete Job Successfully"
          
      }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)




#show and add service
class AddService(APIView):
  def post(self,request):

    try:

      image = request.FILES['image']
      servicename = request.POST['servicename']
      email = request.POST['email']
      contact = request.POST['contact']
      servicecategory = request.POST['category']
      servicedes = request.POST['desc']
      id = request.POST['comapanyid']

      company_id = Company_Account.objects.get(Company_Account_id = id )

      data = Service(Service_Name = servicename, Service_Description = servicedes,Service_Image = image, Email = email,Contact = contact,category = servicecategory,Company_Account_Id = company_id)
      data.save()

      message = {
        'status' : True,
        'message' : "Add Service Successfully"
          
      }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)

  def get(self,request):

    try:

      id = request.GET['comapanyid']
      showservice = Service.objects.filter(Company_Account_Id = id ).order_by('-Service_id')
      if showservice:
        serService = Ser_service(showservice,many=True)
        message = {
          'status' : True,
          'data' : serService.data
            
        }
        return Response(message)

      else:
        message = {
          'status' : False,
          'message' : 'No service is Available'
            
        }
        return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)




##Delete Service
class DeleteService(APIView):
  def get(self,request):

    try:

      id = request.GET['Service_id']
      servicedata = Service.objects.get(Service_id = id)
      servicedata.delete()
      message = {
          'status' : True,
          'message' : 'Delete SuccessFully'
            
        }
      return Response(message)

    except Exception as e:

          
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


class User_CartData(APIView):

  def post(self,request):

    try:
      id = request.data.get('sno')
      data = Order.objects.filter(User_Id = id)
      serorder = Ser_Order(data,many=True)

   

      message = {
        'status' : True,
        'Cart_Data' : serorder.data
            }
                  
      return Response(message)

    except Exception as e:

            
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)



class Product_Locations(APIView):

  def get(self,request):

    try:

      data  = product.objects.all()

      countrylist = []

      for i in data:

          countrylist.append(i.Company_Account_Id.Company_Location.lower())

      message = {
          'status' : True,
          'countrylist' : set(countrylist)
              }
                    
      return Response(message)

    except Exception as e:
      
            
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)


class Service_Locations(APIView):

  def get(self,request):

    try:

      data  = Service.objects.all()

      countrylist = []

      for i in data:

          countrylist.append(i.Company_Account_Id.Company_Location.lower())

      message = {
          'status' : True,
          'countrylist' : set(countrylist)
              }
                    
      return Response(message)

    except Exception as e:
      
            
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)



class Job_Locations(APIView):

  def get(self,request):

    try:

      data  = Job.objects.all()

      countrylist = []

      for i in data:

          countrylist.append(i.Company_Account_Id.Company_Location.lower())

      message = {
          'status' : True,
          'countrylist' : set(countrylist)
              }
                    
      return Response(message)

    except Exception as e:
      
            
      data={
              'status' : False,
              'message': str(e)
          }
      return Response(data)



class User_Cart_Counter(APIView):

  def get(self,request):


    try:

      id = request.GET['sno']
      order_data = Order.objects.filter(User_Id = id)
      if order_data:

        order_count = order_data.count()
        
       
        message = {

              'status' : True,
              'order_count':order_count
          }
        return Response(message)
      else:
          messages.error(request,"Password is Incorrect")
          message = {

              'status' : False,
              'order_count' : 0
          }
          return Response(message)
  
      

    except Exception as e:
            
            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)