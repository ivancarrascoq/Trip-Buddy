from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Trip

class newTrip(forms.Form):
    destination = forms.CharField(min_length=3, max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}) )
    start_date = forms.DateField( widget=forms.TextInput(attrs={'class': "form-control", 'type':"date" }) )
    end_date = forms.DateField( widget=forms.TextInput(attrs={'class': "form-control", 'type':"date" }) )
    plan = forms.CharField(min_length=3, max_length=200, widget=forms.Textarea(attrs={'class': "form-control"}) ) #min_length=3 

class editTrip(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'start_date', 'end_date', 'plan']
        widgets={
                   "start_date":forms.TextInput(attrs={'class': "form-control", 'type':"date" }),
                   "end_date":forms.TextInput(attrs={'class': "form-control", 'type':"date" }),
                   "destination":forms.TextInput(attrs={'class': "form-control"}),
                   "plan":forms.Textarea(attrs={'class': "form-control"})
                } 

class SignupForm(forms.Form):
    first_name = forms.CharField(label='Enter Firstname', min_length=3, max_length=150,
        widget=forms.TextInput(attrs={'class': "form-control", 'id': 'inputfirst1'})
     )
    last_name = forms.CharField(label='Enter Lastname', min_length=3, max_length=150,
            widget=forms.TextInput(attrs={'class': "form-control", 'id': 'inputlast1'})
    )
    username = forms.EmailField(label='Enter Email',
            widget=forms.TextInput(attrs={'class': "form-control", 'id': 'inputEmail1', 'type':'email'})
    )

    password1 = forms.CharField(label='Enter password',
            widget=forms.TextInput(attrs={'class': "form-control", 'id': 'inputPassword1', 'type':'password'})
    )

    password2 = forms.CharField(label='Confirm password',
            widget=forms.TextInput(attrs={'class': "form-control", 'id': 'inputcPassword1', 'type':'password'})
    )

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  forms.ValidationError("Email already exists")
        return username
 
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password don't match")
        return password2
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['password1']
        )
        return user

#class SignupForm2(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
#        widgets={
#            "start_date":forms.TextInput(attrs={'class': "form-control", 'type':"date" }),
#           "end_date":forms.TextInput(attrs={'class': "form-control", 'type':"date" }),
#            "destination":forms.TextInput(attrs={'class': "form-control"}),
#            "plan":forms.Textarea(attrs={'class': "form-control"})
#        } 