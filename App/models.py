from django.db import models


class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Lead(models.Model):
    DESIGNATION_CHOICES = (
        ('Manager', 'Manager'),
        ('Sales Representative', 'Sales Representative'),
        ('Support Agent', 'Support Agent'),
        ('Consultant', 'Consultant'),
        # Add more designations as needed
    )

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=25)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICES)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name} - {self.designation}"

class CustomerQuery(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    query_text = models.TextField()
    lead_assigned = models.ForeignKey('Lead', on_delete=models.SET_NULL, null=True, blank=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Query from {self.customer.full_name} - {self.resolved}"