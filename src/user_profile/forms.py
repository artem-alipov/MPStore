from django import forms
from .models import CustomerProfile, Address
from django.forms.models import modelform_factory

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('country', 'city', 'postal_code', 'address_line_1', 'address_line_2')

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ('email_profile', 'first_profile_name', 'last_profile_name', 'phone', 'group', 'additional_info')
















# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = CustomerProfile
#         fields = [
#             'email_profile',
#             'first_profile_name',
#             'last_profile_name',
#             'phone',
#             'group',
#             'address',
#             'additional_info'
#         ]
        
#     def __init__(self, user, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         self.fields['address'].queryset = Address.objects.filter(user=user)
        
#     def save(self, commit=True):
#         instance = super(UserProfileForm, self).save(commit=False)
        
#         address = self.cleaned_data['address']
#         instance.address = address
#         instance.save()
        
#         return instance


# class AddressForm(forms.ModelForm):
#     class Meta:
#         model = Address
#         fields = [
#             'country',
#             'city',
#             'postal_code',
#             'address_line_1',
#             'address_line_2',
#         ]



# AddressForm = modelform_factory(
#     Address, 
#     fields=[
#             'user',
#             'country',
#             'city',
#             'postal_code',
#             'address_line_1',
#             'address_line_2',
#             ])

# class UserProfileForm(forms.ModelForm):
#     address = AddressForm()
    
#     class Meta:
#         model = CustomerProfile
#         fields = [
#             'email_profile',
#             'first_profile_name',
#             'last_profile_name',
#             'phone', 
#             'group', 
#             'address',
#             'additional_info'
#             ]
        
#     def __init__(self, user, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         self.instance = CustomerProfile.objects.get(user=user)
#         self.fields['email_profile'].initial = self.instance.email_profile
#         self.fields['first_profile_name'].initial = self.instance.first_profile_name
#         self.fields['last_profile_name'].initial = self.instance.last_profile_name
#         self.fields['phone'].initial = self.instance.phone
#         self.fields['group'].initial = self.instance.group
#         self.fields['additional_info'].initial = self.instance.additional_info

#     def save(self, commit=True):
#         self.instance.email_profile = self.cleaned_data['email_profile']
#         self.instance.first_profile_name = self.cleaned_data['first_profile_name']
#         self.instance.last_profile_name = self.cleaned_data['last_profile_name']
#         self.instance.phone = self.cleaned_data['phone']
#         self.instance.group = self.cleaned_data['group']
#         self.instance.additional_info = self.cleaned_data['additional_info']
        
#         if commit:
#             self.instance.save()

#         return self.instance