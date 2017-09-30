from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    CUSTOMER_TYPE_CHOICES = (
        (0, 'INDIVIDUAL'),
        (1, 'COMMERCIAL'),
    )
    customer_type = models.IntegerField(choices=CUSTOMER_TYPE_CHOICES)

    def __str__(self):
        return 'Customer {}: {} -- {}'.format(self.id, self.name, self.email)

class Invoice(models.Model):
    customer = models.ForeignKey(Customer)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
