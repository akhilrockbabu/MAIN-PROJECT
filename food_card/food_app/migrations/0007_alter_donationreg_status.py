# Generated by Django 4.1.4 on 2023-04-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0006_donationreg_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationreg',
            name='status',
            field=models.DateField(max_length=40, null=True),
        ),
    ]
