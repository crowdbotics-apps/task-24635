from django.contrib import admin
from .models import (
    PaymentTransaction,
    TaskerPaymentAccount,
    TaskerWallet,
    PaymentMethod,
    CustomerWallet,
)

admin.site.register(TaskerWallet)
admin.site.register(PaymentTransaction)
admin.site.register(TaskerPaymentAccount)
admin.site.register(PaymentMethod)
admin.site.register(CustomerWallet)

# Register your models here.
