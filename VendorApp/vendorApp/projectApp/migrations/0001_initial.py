# Generated by Django 4.2.7 on 2024-05-09 04:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('vendor_code', models.CharField(max_length=20, unique=True)),
                ('on_time_delivery_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('quality_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('response_time', models.DurationField(blank=True, null=True)),
                ('fulfilment_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=50)),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('quality_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectApp.vendor')),
            ],
        ),
    ]