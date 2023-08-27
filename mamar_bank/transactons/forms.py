from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount','transaction_type']
    
    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True  # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() #user theke hide thakbe
    
    def save(self,commit =True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()
    
class DepositForm(TransactionForm):
    def clean_amount(self):
        min_deposit = 100
        amount = self.cleaned_data.get('amount')
        if amount < min_deposit:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit} $'
            )
        return amount

class WithdrawForm(TransactionForm):
    def clean_amount(self):
        account = self.account
        min_withdraw = 500
        max_withdraw = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw} $'
            )
        if amount > max_withdraw:
            raise forms.ValidationError(
                f'You can not withdraw more than {max_withdraw} $'
            )
        if amount > balance:
            raise forms.ValidationError(
                f'you have {balance} in your account. '
                'you can not withdraw more than your account balance'
            )
            
        return amount
class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        return amount
