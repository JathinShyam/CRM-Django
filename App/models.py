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
    # query = models.ForeignKey('CustomerQuery', on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}"


class Employee(models.Model):
    DESIGNATION_CHOICES = (
        ("Customer Support Representative","Customer Support Representative"),
        ("Product Specialist","Product Specialist"),
        ("Marketing Coordinator","Marketing Coordinator"),
        ("IT Support Technician","IT Support Technician"),
        ("Financial Analyst","Financial Analyst"),
        ("Logistics Coordinator","Logistics Coordinator"),
        ("Lead", "Lead"),
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
    QUERY_TYPES = (
        ("Product Inquiries", "Product Inquiries"),
        ("Order Status and Tracking", "Order Status and Tracking"),
        ("Complaints", "Complaints"),
        ("Returns and Refunds", "Returns and Refunds"),
        ("Payment Issues", "Payment Issues"),
        ("Account Management", "Account Management"),
        ("Technical Support", "Technical Support"),
        ("Offers and Promotions", "Offers and Promotions"),
        ("Feedback and Suggestions", "Feedback and Suggestions"),
        ("General Inquiries", "General Inquiries"),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    query = models.CharField(max_length=50, choices=QUERY_TYPES, default="General Inquiries")
    query_text = models.TextField()
    employee_assigned = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    resolved = models.BooleanField(default=False)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"Query from {self.customer.full_name} - {self.resolved}"