from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    employment_status = models.CharField(max_length=50)
    annual_income = models.DecimalField(max_digits=12, decimal_places=2)
    credit_score = models.PositiveIntegerField()
    # Add more fields related to customer details required for a loan

class LoanProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    maximum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    minimum_amount = models.DecimalField(max_digits=12, decimal_places=2)
    minimum_credit_score = models.PositiveIntegerField()
    repayment_terms = models.PositiveIntegerField(help_text="In months")
    required_documents = models.TextField(help_text="List of required documents")
    # Add more fields related to the loan product details

class LoanApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_product = models.ForeignKey(LoanProduct, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    duration_months = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    application_date = models.DateTimeField(auto_now_add=True)
    coapplicant_name = models.CharField(max_length=255, blank=True, null=True)
    coapplicant_income = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    # Add more fields related to the loan application details

class FinanceBlog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='blogs')
    featured_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    # Add more fields related to finance blog details

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # Add more fields as needed

# Additional models can be added as necessary based on the specific requirements of the website.


class Feedback(models.Model):
    NAME_AS_ON_PANCARD = models.CharField(max_length=20)
    PERSONAL_EMAIL_ID = models.CharField(max_length=20)
    MOBILE_NUMBER = models.IntegerField()
    SUBJECT_LINE = models.CharField(max_length=20)
    Write_Message = models.BooleanField()


class Employee(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    salary = models.IntegerField()
    dept = models.IntegerField()
    role = models.CharField(max_length=20)
    bonus = models.IntegerField()


class Loan_apply(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    amount = models.IntegerField()
    term = models.IntegerField()

class Login_user(models.Model):
    username = models.CharField(max_length=20)
    password = models.IntegerField()

class Signup_user(models.Model):
    username = models.CharField(max_length=20)
    Email = models.EmailField()
    password = models.IntegerField()
    Confirm_Password = models.IntegerField()
    
   

   