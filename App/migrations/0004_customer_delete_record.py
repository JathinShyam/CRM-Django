# Generated by Django 4.2.4 on 2023-09-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App", "0003_alter_record_email_alter_record_phone_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.CharField(max_length=25)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("pincode", models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name="Record",
        ),
    ]
