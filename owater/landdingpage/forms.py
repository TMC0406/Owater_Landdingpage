from django import forms

class formInfo(forms.Form):
    username  = forms.CharField()
    phone = forms.CharField()
    address = forms.CharField()
    province = forms.CharField()
    email = forms.CharField()
    note = forms.CharField()
    dataOder = forms.CharField()
    total = forms.CharField()





