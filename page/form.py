from django import forms  

class uform(forms.Form):
        First_name = forms.CharField(label ='First_name',widget=forms.TextInput(attrs={'class':"form-control"}))
        Last_name = forms.CharField(label ='Last_name',widget=forms.TextInput(attrs={'class':"form-control"}))
        Email = forms.EmailField(label ='Email',widget=forms.TextInput(attrs={'class':"form-control"}))
        Bio = forms.CharField(label ='Bio',widget=forms.TextInput(attrs={'class':"form-control"}))
        Gender = forms.CharField(label ='Gender',widget=forms.TextInput(attrs={'class':"form-control"}))
        Phone = forms.IntegerField(label ='Phone')
        Address = forms.CharField(label ='Address',widget=forms.TextInput(attrs={'class':"form-control"}))
        City = forms.CharField(label ='City',widget=forms.TextInput(attrs={'class':"form-control"}))
        State = forms.CharField(label ='State',widget=forms.TextInput(attrs={'class':"form-control"}))
        Country = forms.CharField(label ='Country',widget=forms.TextInput(attrs={'class':"form-control"}))
        Zipcode = forms.IntegerField(label ='Zipcode')
        # image = forms.ImageField(upload_to='')
