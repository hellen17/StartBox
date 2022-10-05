from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.core.validators import RegexValidator



NATURE_OF_BUSINESS= [
    ('online business', 'Online Business'),
    ('SME', 'Small Medium Enterpise (SME)'),
    ('startup', 'Startup'),
   
    ]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name', max_length=150)
    last_name = forms.CharField(label='Last Name', max_length=150)
    # phone_regex = RegexValidator(regex=r'(\+254)\s*?(\d{3})\s*?(\d{3})\s*?(\d{3})', message="invalid phone number, phone number should be in the format of +254")
    # phone_number = forms.CharField(validators=[phone_regex], max_length=13, widget=forms.TextInput(attrs={'placeholder': 'Use the format: \'+2547xxxxxxxx\''})) # validators should be a list

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

# class CustomUserCreationForm(UserCreationForm):  
#     username = forms.CharField(label='Username', min_length=5, max_length=150)  
#     email = forms.EmailField(label='Email')  
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  
  
#     def username_clean(self):  
#         username = self.cleaned_data['username'].lower()  
#         new = User.objects.filter(username = username)  
#         if new.count():  
#             raise ValidationError("User Already Exist")  
#         return username  
  
#     def email_clean(self):  
#         email = self.cleaned_data['email'].lower()  
#         new = User.objects.filter(email=email)  
#         if new.count():  
#             raise ValidationError(" Email Already Exist")  
#         return email  
  
#     def clean_password2(self):  
#         password1 = self.cleaned_data['password1']  
#         password2 = self.cleaned_data['password2']  
  
#         if password1 and password2 and password1 != password2:  
#             raise ValidationError("Password don't match")  
#         return password2  
  
#     def save(self, commit = True):  
#         user = User.objects.create_user(  
#             self.cleaned_data['username'],  
#             self.cleaned_data['email'],  
#             self.cleaned_data['password1']  
#         )  
#         return user  




class ContactForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    #nature_of_business = forms.CharField(widget=forms.Select(choices=NATURE_OF_BUSINESS))
    contact_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()

    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))