from django import forms

from djtest.models import Customer


class CustomerEditForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            'name',
            'email',
            'phone',
            'customer_type',
        )
