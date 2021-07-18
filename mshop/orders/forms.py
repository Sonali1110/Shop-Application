from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']
        widget = {
         'first_name': forms.TextInput(attrs={'placeholder': ' First Name'},),
            'last_name': forms.TextInput(attrs={'class': 'form-control custom-class'}),

        #  'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
        # 'address': forms.Textarea(attrs={'class': 'form-control'}),
        # 'postal_cod': forms.TextInput(attrs={'class': 'form-control'}),
        # 'city': forms.TextInput(attrs={'class': 'form-control'}),
         }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address',
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('postal_code', css_class='form-group col-md-2 mb-0'),
                Column('city', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        )
