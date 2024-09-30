from django import forms
class Login(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email','style':'width:210px;color:blue'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','style':'width:210px;color:blue'
    }))

#register form
class Register(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your name','style':'width:210px;color:blue'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email','style':'width:210px;color:blue'
    }))
    phone_number = forms.IntegerField(widget=forms.TextInput(attrs={
        'placeholder':'Your phone number','style':'width:210px;color:blue'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','style':'width:210px;color:blue'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password','style':'width:210px;color:blue'
    }), label='Repeat password')

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search...'}))