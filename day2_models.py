from django.db import models #include

class product(models.Model):
    sku=models.CharField(max_length=10,primary_key=True)
    
    title=models.CharField(max_lengh=255) #varchar(255)
    description=models.TextField()
    price=models.models.DecimalField(max_digits=6 , decimal_palces=2)
    inventory = models.IntegerField()
    last_updates=models.DateTimeField(auto_now_add=True)


class customer(models.Model):
    
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    
    MEMBERSHIP_CHOICES=[         ## this will not change
        ('MEMBERSHIP_BRONZE','Bronze'),
        ('MEMBERSHIP_SILVER','silver'),
        ('MEMBERSHIP_GOLD','gold'),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    birth_day=models.DateField(null=True)
    
    membership=models.CharField(max_length=1 ,choices=MEMBERSHIP_CHOICES ,default=MEMBERSHIP_BRONZE)
    
class payment(models.Model):
    
    PAYMENT_STATUS_PENDING='P'
    PAYMENT_STATUS_FAILED='F'
    PAYMENT_STATUS_COMPLETED='C'
    PAYMENT_STATUS_CHOICES=[
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_FAILED,'Failed'),
        (PAYMENT_STATUS_COMPLETED,'Completed')
        ]
    
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(
        max_length=1,choices= PAYMENT_STATUS_CHOICES ,default=PAYMENT_STATUS_PENDING
    )
