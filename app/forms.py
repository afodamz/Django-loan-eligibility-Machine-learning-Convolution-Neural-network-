from django import forms
from .models import UserLoan

class UserLoanForm(forms.ModelForm):
    Email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs = {
        'class': 'my-super-special-input',
        'placeholder': "mailbox@example.com"
    }),
    )

    class Meta:
        model = UserLoan
        fields = '__all__'
