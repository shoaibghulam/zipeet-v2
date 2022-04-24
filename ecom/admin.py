
from django.contrib import admin
from app.models import product,category,User_Signup,Contact,Order,Company_Account,Service,Job,User_Contatact_Job,User_Contatact_Service
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    
    list_display=('name','category','stock','price')

# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy

# class MyEcmomsite(AdminSite):
#     site_title = ugettext_lazy('Django site admin')
#     site_header = ugettext_lazy('Zipeet')
#     index_title = ugettext_lazy('Admin Panel')

# ecmo_admin_site = MyEcmomsite()

admin.site.register(product,ProductAdmin)
admin.site.register(category)
admin.site.register(User_Signup)
admin.site.register(Contact)
admin.site.register(Order)

admin.site.register(Company_Account)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(User_Contatact_Service)
admin.site.register(User_Contatact_Job)
