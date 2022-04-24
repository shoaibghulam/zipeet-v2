from rest_framework import serializers
from app.models import product,category,User_Signup,Contact,Order,Company_Account,Service,Job,User_Contatact_Job,User_Contatact_Service,Ser_product,Ser_service,Ser_job,Ser_account,Ser_cat







class SerCompany_Account(serializers.ModelSerializer):
    class Meta:
        model = Company_Account
        
        fields = '__all__'


class DynamicSerCompany_Account(serializers.ModelSerializer):
    class Meta:
        model = Company_Account
        
        fields = ['Company_Account_id','Company_Account_Name','Company_Account_Email','Company_Account_logo','Company_Account_Desc','Contact','Company_Adress','Company_Whatsapp_No','Company_Location','Service_Category']