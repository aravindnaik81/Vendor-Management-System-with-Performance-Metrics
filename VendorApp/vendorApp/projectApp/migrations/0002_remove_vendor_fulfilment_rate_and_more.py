# Generated by Django 4.2.7 on 2024-05-09 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='fulfilment_rate',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='quality_rating',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='response_time',
        ),
        migrations.AddField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='delivery_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='issue_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='quality_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectApp.vendor')),
            ],
        ),
    ]
