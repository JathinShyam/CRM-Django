# Generated by Django 4.2.4 on 2023-10-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0006_customerquery_query"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="designation",
            field=models.CharField(
                choices=[
                    ("Delivery Handler", "Delivery Handler"),
                    (
                        "Customer Support Representative",
                        "Customer Support Representative",
                    ),
                    ("Sales Associate", "Sales Associate"),
                    ("Product Specialist", "Product Specialist"),
                    ("Marketing Coordinator", "Marketing Coordinator"),
                    ("IT Support Technician", "IT Support Technician"),
                    ("Product Manager", "Product Manager"),
                    ("Web Developer", "Web Developer"),
                    ("Financial Analyst", "Financial Analyst"),
                    ("Logistics Coordinator", "Logistics Coordinator"),
                    ("Inventory Manager", "Inventory Manager"),
                ],
                max_length=50,
            ),
        ),
    ]
