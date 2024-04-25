from django.contrib import admin
from .models import Feedback,Employee,Loan_apply,Login_user,Signup_user
from .models import Customer,LoanProduct,LoanApplication,FinanceBlog,Tag

class Signup_userAdmin(admin.ModelAdmin):
    list_display = ("username", "Email", "password", "Confirm_Password")

class Login_userAdmin(admin.ModelAdmin):
    list_display = ("username","password")

class Loan_applyAdmin(admin.ModelAdmin):
    list_display = ("name","email", "amount", "term")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","last_name","salary", "dept", "role", "bonus")

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("NAME_AS_ON_PANCARD","PERSONAL_EMAIL_ID","MOBILE_NUMBER","SUBJECT_LINE","Write_Message")


# Register your models here.
admin.site.register(Customer)
admin.site.register(LoanProduct)
admin.site.register(LoanApplication)
admin.site.register(FinanceBlog)
admin.site.register(Tag)

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Loan_apply,Loan_applyAdmin)
admin.site.register(Login_user,Login_userAdmin)
admin.site.register(Signup_user,Signup_userAdmin)

