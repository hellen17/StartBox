from django import forms

NATURE_OF_BUSINESS= [
    ('online business', 'Online Business'),
    ('SME', 'Small Medium Enterpise (SME)'),
    ('startup', 'Startup'),
   
    ]


class ContactForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    nature_of_business = forms.CharField(widget=forms.Select(choices=NATURE_OF_BUSINESS))
    contact_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    email = forms.EmailField()

    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))