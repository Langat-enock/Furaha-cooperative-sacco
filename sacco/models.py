import os
import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


def generate_unique_name(instance, filename):
    name = uuid.uuid4() #
    full_file_name = f'{name}-{filename}'
    return os.path.join("profile_pictures", full_file_name)

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.gender}"

    class Meta:
        db_table = 'customers'

class Deposit(models.Model):
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='deposits')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.first_name} - {self.amount}"

    class Meta:
        db_table = 'deposits'



    class Transaction(models.Model):
        TRANSACTION_TYPE_CHOICES = [
            ('DEPOSIT', 'Deposit'),
            ('WITHDRAWAL', 'Withdrawal'),
        ]


        transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
        amount = models.DecimalField(max_digits=10, decimal_places=2)
        timestamp = models.DateTimeField(auto_now=now)

        # def __str__(self):
        #     return f"{self.wallet.user.username} - {self.transaction_type} - {self.amount}"





# run the migrations
# python manage.py makemigrations
# python manage.py migrate

# python manage.py populate
def customer():
    return None