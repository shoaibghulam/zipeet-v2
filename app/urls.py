from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="HomePage"),
    path('allproduct',views.allproduct,name="allproduct"),
    path('product/<int:myid>',views.products,name="ProductView"),
    path("category/<int:cid>",views.categories,name="Master"),
    # path("addtocart/<int:proid>",views.updatecart,name="updatecart"),
    # path("removecart/<int:cartid>",views.removecart,name="Removecart"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    # path('cart',views.cart,name="Cart"),
    path('logout',views.logout,name="logout"),
    path('contact',views.contact,name="contact"),
    path('tracker',views.tracker,name="tracker"),
    path('search',views.search,name="search"),
    path('checkout/<int:id>',views.checkout,name="Checkout"),
    path('allservices',views.allservices,name="allservices"),
    path('serviceview/<int:id>',views.serviceview,name="serviceview"),
    path('alljob',views.alljob,name="alljob"),
    path('jobview/<int:id>',views.jobview,name="jobview"),
    path('servicecontact/<int:id>',views.servicecontact,name="servicecontact"),
    path('jobcontact/<int:id>',views.jobcontact,name="jobcontact"),
    path('serviceprovideraccount',views.serviceprovideraccount,name="serviceprovideraccount"),
    path('serviceproviderlogin',views.serviceproviderlogin,name="serviceproviderlogin"),
    path('companylogout',views.companylogout,name="companylogout"),

    path('Usercontact',views.Usercontact,name="Usercontact"),
    path('deletecontact',views.deletecontact,name="deletecontact"),
    path('companyaccount',views.companyaccount,name="companyaccount"),
    path('editaccount',views.editaccount,name="editaccount"),
    path('contactjobs',views.contactjobs,name="contactjobs"),
    path('deletejobs',views.deletejobs,name="deletejobs"),
    path('contactservices',views.contactservices,name="contactservices"),
    path('deleteservices',views.deleteservices,name="deleteservices"),
    path('productorder',views.productorder,name="productorder"),
    path('deleteproductorder',views.deleteproductorder,name="deleteproductorder"),
    path('productcategory',views.productcategory,name="productcategory"),
    path('addproductcategory',views.addproductcategory,name="addproductcategory"),
    path('deleteproductcategory',views.deleteproductcategory,name="deleteproductcategory"),
    path('editproductcategory',views.editproductcategory,name="editproductcategory"),
    path('exportproducts',views.exportproducts,name="exportproducts"),
    path('exportservice',views.exportservice,name="exportservice"),
    path('exportjob',views.exportjob,name="exportjob"),
    path('userforget',views.userforget,name="userforget"),
    path('companyforget',views.companyforget,name="companyforget"),
 
    





    ####suggestion search#######
    path('locationsearch',views.locationsearch,name="locationsearch"),
    path('productnamesearch',views.productnamesearch,name="productnamesearch"),
    path('jobnamesearch',views.jobnamesearch,name="jobnamesearch"),
    path('servicenamesearch',views.servicenamesearch,name="servicenamesearch"),



    path('suggestioncheck',views.suggestioncheck,name="suggestioncheck"),






    




















######admin############


    path('serviceprovider',views.serviceprovider,name="serviceprovider"),
    path('adminproducts',views.adminproducts,name="adminproducts"),
    path('deleteproducts/<int:id>',views.deleteproducts,name="deleteproducts"),
    path('services',views.services,name="services"),
    path('jobs',views.jobs,name="jobs"),
    path('carts',views.carts,name="carts"),
    
    
    
    
    path('servicecategory',views.servicecategory,name="servicecategory"),
    
    path('contactservices',views.contactservices,name="contactservices"),
    path('contactjobs',views.contactjobs,name="contactjobs"),
    path('edit_product',views.edit_product,name="edit_product"),
    path('deleteservice/<int:id>',views.deleteservice,name="deleteservice"),
    path('edit_service',views.edit_service,name="edit_service"),
    path('deletejob/<int:id>',views.deletejob,name="deletejob"),
    path('edit_job',views.edit_job,name="edit_job"),









     path('checking',views.checking,name="checking"),


    


    
 

]