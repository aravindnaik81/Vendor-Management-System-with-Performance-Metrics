# Generated by Django 4.2.7 on 2024-05-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0002_remove_vendor_fulfilment_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='expected_delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
