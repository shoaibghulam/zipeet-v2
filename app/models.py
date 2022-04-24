from django.db import models
from rest_framework import serializers
# Order CHoices
STATUS_CHOICES =(
        ("Delivered","Delivered"),
        ("NotDelivered","NotDelivered"),
        ("reject","Reject"),
    )
PRODUCT_CATEGORY =(
        ("weeklyoffer","Weekly Offers"),
        ("hotoffers","Hot offers"),
        ("Nooffer","No Offer"),
        
    )
Service_Catego =(
        ("product","Products Sale"),
        ("service","Service"),
        ("jobs","Jobs"),
        
    )
Service =(
        ("daily","Daily"),
        ("monthly","Monthly"),
        ("yearly","Yearly"),
        
    )
Job_Cat =(
        ("highpaidjobs","High Paid Jobs"),
        ("recentjob","Recent job"),
        ("parttimejob","Parttime Job"),
        
    )

# Create your models here.


   

class Company_Account(models.Model):
    Company_Account_id= models.AutoField(primary_key=True)
    Company_Account_Name=models.CharField(max_length=200,default="Name")
    Company_Account_Email=models.EmailField()
    password=models.CharField(max_length=100,default="password")
    Company_Account_logo=models.ImageField(upload_to='CompanyAccount/',default='mypic')
    Company_Account_Desc=models.TextField(default="Desc")
    Contact=models.CharField(max_length=120,default="contact" )
    created_At=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Company_Adress=models.TextField(default="Adress")
    Company_Whatsapp_No=models.CharField(max_length=120,default="0")
    Company_Location=models.CharField(max_length=100,default="location" )
    Service_Category=models.CharField(max_length=100, default="product",choices=Service_Catego)
   

class Ser_account(serializers.ModelSerializer):
    class Meta:
        model = Company_Account
        fields = '__all__'

class category(models.Model):
    cid=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=100)
    Company_Account_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)
    def __str__(self):
        return self.cname

class Ser_cat(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'

class product(models.Model):
    pid= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    category= models.ForeignKey(category, on_delete=models.CASCADE)
    price= models.CharField(max_length=1000,default=0)
    stock=models.IntegerField(default=0)
    description=models.TextField(default="Dummay Description")
    image=models.ImageField(upload_to='Products/',default='mypic')
    Product_offers=models.CharField(max_length=120, choices=PRODUCT_CATEGORY, default="Nooffer")
    Company_Account_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)

class Ser_product(serializers.ModelSerializer):
    # category_id = serializers.ReadOnlyField(source='category.cid')

    class Meta:
        model = product
        fields = '__all__'


 

class Service(models.Model):
    Service_id= models.AutoField(primary_key=True)
    Service_Name=models.CharField(max_length=200,default="Name")
    Service_Description=models.TextField(default="Desc")
    Service_Image=models.ImageField(upload_to='Sevice/',default='mypic')
    Service_Date=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Email=models.EmailField()
    Contact=models.CharField(max_length=120,default="contact" )
    category=models.CharField(max_length=120, choices=Service, default="product")
    Company_Account_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.Service_Name
    

class Ser_service(serializers.ModelSerializer):


    class Meta:
        model = Service
        fields = '__all__'




class Job(models.Model):
    Job_id= models.AutoField(primary_key=True)
    Job_Name=models.CharField(max_length=200,default="Name")
    Job_Description=models.TextField(default="Desc")
    Job_Image=models.ImageField(upload_to='Job/',default='mypic')
    Job_Date=models.DateTimeField(auto_now_add=True,blank=True, null=True)
    Experience_Required=models.CharField(max_length=120,default="0" )
    Email=models.EmailField()
    Contact=models.CharField(max_length=120,default="contact" )
    category=models.CharField(max_length=120, choices=Job_Cat, default="product")
    Company_Account_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)


    def __str__(self):
        return self.Job_Name
    

class Ser_job(serializers.ModelSerializer):


    class Meta:
        model = Job
        fields = '__all__'





class User_Signup(models.Model):
    sno = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    Whatsapp_No=models.CharField(max_length=120,default="0")
    Contact_No=models.CharField(max_length=120,default="0")
    Location=models.CharField(max_length=100,default="location" )


class Ser_Signup(serializers.ModelSerializer):


    class Meta:
        model = User_Signup
        fields = '__all__'


    
# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add = True , blank = True)

    def __str__(self):
        return self.name


# Order items
class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    Ordertime=models.TimeField(auto_now_add=True,blank=True, null=True)
    status=models.CharField(max_length=120, choices=STATUS_CHOICES, default="Started")   
    timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)
    update=models.DateTimeField(auto_now_add=False, auto_now=True)
    Firstname=models.CharField(max_length=120 ,default="Dummay")
    lastname=models.CharField(max_length=120 ,default="Dummay")
    phoneno=models.CharField(max_length=120 ,default="Dummay")
    emailid=models.CharField(max_length=120 ,default="Dummay")
    address=models.CharField(max_length=120 ,default="Dummay")
    city=models.CharField(max_length=120 ,default="Dummay")
    district=models.CharField(max_length=120 ,default="Dummay")
    zipcode=models.CharField(max_length=120 ,default="Dummay")
    User_Id=models.ForeignKey(User_Signup, on_delete=models.CASCADE,blank=True, null=True)
    tokenid=models.CharField(max_length=120 ,default="Dummay")
    totalamount=models.FloatField(default=0.00)
    Product_Quantity=models.FloatField(max_length=120 ,default=0)
    Product_id=models.ForeignKey(product, on_delete=models.CASCADE,blank=True, null=True)
    Company_Account_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)
    
    def __str__(self):
        return self.Firstname


class Ser_Order(serializers.ModelSerializer):

    name = serializers.ReadOnlyField(source="User_Id.name")
    phone = serializers.ReadOnlyField(source="User_Id.phone")
    email = serializers.ReadOnlyField(source="User_Id.email")
    content = serializers.ReadOnlyField(source="User_Id.content")
    Company_Account_Name = serializers.ReadOnlyField(source="Company_Account_Id.Company_Account_Name")
    Company_Account_Email = serializers.ReadOnlyField(source="Company_Account_Id.Company_Account_Email")
    Company_Account_logo = serializers.ReadOnlyField(source="Company_Account_Id.Company_Account_logo.url")
    Company_Account_Desc = serializers.ReadOnlyField(source="Company_Account_Id.Company_Account_Desc")
    Company_Account_Contact = serializers.ReadOnlyField(source="Company_Account_Id.Contact")
    Company_Adress = serializers.ReadOnlyField(source="Company_Account_Id.Company_Adress")
    Company_Whatsapp_No = serializers.ReadOnlyField(source="Company_Account_Id.Company_Whatsapp_No")
    Company_Location = serializers.ReadOnlyField(source="Company_Account_Id.Company_Location")
    Product_name = serializers.ReadOnlyField(source="Product_id.name")
    Service_Category_Name = serializers.ReadOnlyField(source="Company_Account_Id.Service_Category")
    
    

    class Meta:
        model = Order
        fields = ('order_id','Ordertime','status','timestamp','update','Firstname','lastname','phoneno','emailid','address','city','district','zipcode','totalamount','Product_Quantity','User_Id','name','phone','email','content','Company_Account_Id','Company_Account_Name','Company_Account_Email','Company_Account_logo','Company_Account_Desc','Company_Account_Contact','Company_Adress','Company_Whatsapp_No','Company_Location','Service_Category_Name','Product_name')
   
   
class User_Contatact_Service(models.Model):
    User_Contatact_Service_id=models.AutoField(primary_key=True)
    User_Id=models.ForeignKey(User_Signup, on_delete=models.CASCADE,blank=True, null=True)
    fname = models.CharField(max_length=255,default="Name")
    lname = models.CharField(max_length=100,default="Name")
    email = models.EmailField(max_length=50,default="Email")
    password=models.CharField(max_length=100,default="Password")
    address=models.CharField(max_length=120 ,default="adress")
    city=models.CharField(max_length=120 ,default="City")
    district=models.CharField(max_length=120 ,default="District")
    phoneno=models.CharField(max_length=120 ,default="No")
    Whatsapp_No=models.CharField(max_length=120 ,default="No")
    Location=models.CharField(max_length=100,default="location" )
    Desc=models.TextField(default="Desc")
    Comapnay_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)
    Service_id=models.ForeignKey(Service, on_delete=models.CASCADE,blank=True, null=True)

class User_Contatact_Job(models.Model):
    User_Contatact_Job_id=models.AutoField(primary_key=True)
    User_Id=models.ForeignKey(User_Signup, on_delete=models.CASCADE,blank=True, null=True)
    fname = models.CharField(max_length=255,default="Name")
    lname = models.CharField(max_length=100,default="Name")
    email = models.EmailField(max_length=50,default="Email")
    password=models.CharField(max_length=100,default="Password")
    address=models.CharField(max_length=120 ,default="adress")
    city=models.CharField(max_length=120 ,default="City")
    district=models.CharField(max_length=120 ,default="District")
    phoneno=models.CharField(max_length=120 ,default="No")
    Whatsapp_No=models.CharField(max_length=120 ,default="No")
    Location=models.CharField(max_length=100,default="location" )
    Desc=models.TextField(default="Desc")
    Comapnay_Id=models.ForeignKey(Company_Account, on_delete=models.CASCADE,blank=True, null=True)
    Job_id=models.ForeignKey(Job, on_delete=models.CASCADE,blank=True, null=True)