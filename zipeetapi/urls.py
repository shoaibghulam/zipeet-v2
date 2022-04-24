from django.urls import path,include
from zipeetapi.views import navBarData,Products,dailyService,monthlyService,yearlyService,recentJobs,parttimeJobs,highpaidJobs,Show_All_Products,Show_All_Services,Show_All_Jobs,View_Product,View_Service,View_Job,View_Category_Data,Customer_Contact,Products_Search,User_signUp,User_Login,Checkout,Job_Search,Service_Search,companyAccountSignup,companyAccountLogin,AddProductCategory,showProductCategory,deleteCategory,AddProducts,DeleteProduct,AddJobs,DeleteJob,AddService,DeleteService,servicecontact,jobcontact,User_CartData,Product_Locations,Service_Locations,Job_Locations,User_Cart_Counter

urlpatterns = [
    

    path('navBarData',navBarData.as_view()),
    path('Products',Products.as_view()),
    path('dailyService',dailyService.as_view()),
    path('monthlyService',monthlyService.as_view()),
    path('yearlyService',yearlyService.as_view()),
    path('recentJobs',recentJobs.as_view()),
    path('parttimeJobs',parttimeJobs.as_view()),
    path('highpaidJobs',highpaidJobs.as_view()),
    path('Show_All_Products',Show_All_Products.as_view()),
    path('Show_All_Services',Show_All_Services.as_view()),
    path('Show_All_Jobs',Show_All_Jobs.as_view()),
    path('View_Product',View_Product.as_view()),
    path('View_Service',View_Service.as_view()),
    path('View_Job',View_Job.as_view()),
    path('View_Category_Data',View_Category_Data.as_view()),
    path('Customer_Contact',Customer_Contact.as_view()),
    path('Products_Search',Products_Search.as_view()),
    path('User_signUp',User_signUp.as_view()),
    path('User_Login',User_Login.as_view()),
    path('Checkout',Checkout.as_view()),
    path('Job_Search',Job_Search.as_view()),
    path('Service_Search',Service_Search.as_view()),
    path('servicecontact',servicecontact.as_view()),
    path('jobcontact',jobcontact.as_view()),


    ##shakeeb work

    path('companyAccountSignup',companyAccountSignup.as_view()),
    path('companyAccountLogin',companyAccountLogin.as_view()),
    path('AddProductCategory',AddProductCategory.as_view()),
    path('showProductCategory',showProductCategory.as_view()),
    path('deleteCategory',deleteCategory.as_view()),
    path('AddProducts',AddProducts.as_view()),
    path('DeleteProduct',DeleteProduct.as_view()),
    path('AddJobs',AddJobs.as_view()),
    path('DeleteJob',DeleteJob.as_view()),
    path('AddService',AddService.as_view()),
    path('DeleteService',DeleteService.as_view()),
    path('User_CartData',User_CartData.as_view()),
    path('Product_Locations',Product_Locations.as_view()),
    path('Service_Locations',Service_Locations.as_view()),
    path('Job_Locations',Job_Locations.as_view()),
    path('User_Cart_Counter',User_Cart_Counter.as_view()),



]