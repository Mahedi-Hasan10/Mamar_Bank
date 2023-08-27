from django.db import models
from accounts.models import UserBankAccount
# Create your models here.
from transactons.constants import TRANSACTOIN_TYPE

class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name='transaction', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2,max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2,max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTOIN_TYPE,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approval = models.BooleanField(default=False)
    class Meta:
        ordering = ['timestamp']
