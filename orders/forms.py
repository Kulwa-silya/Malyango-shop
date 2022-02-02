from django import forms
from .models import Order
from material import Layout, Row 

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['f_name', 'l_name', 'email', 'address', 'city']
    layout = Layout(
        Row('f_name', 'l_name'),
        'email',
        'address',
        'city'
    )