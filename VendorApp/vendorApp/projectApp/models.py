from django.db import models
from django.utils import timezone


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    #response_time_avg = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name

    def calculate_on_time_delivery_rate(self):
        completed_orders = self.purchaseorder_set.filter(status='completed')
        on_time_orders = completed_orders.filter(delivery_date__lte=models.F('expected_delivery_date'))
        total_orders = completed_orders.count()
        on_time_rate = (on_time_orders.count() / total_orders) * 100 if total_orders > 0 else 0
        return round(on_time_rate, 2)

    def calculate_quality_rating_average(self):
        completed_orders_with_ratings = self.purchaseorder_set.filter(status='completed', quality_rating__isnull=False)
        rating_average = completed_orders_with_ratings.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
        return round(rating_average, 2) if rating_average else 0

    def calculate_average_response_time(self):
        completed_orders_with_acknowledgment = self.purchaseorder_set.filter(status='completed', acknowledgment_date__isnull=False)
        response_times = completed_orders_with_acknowledgment.annotate(
            response_time=models.ExpressionWrapper(
                models.F('acknowledgment_date') - models.F('issue_date'),
                output_field=models.DurationField()
            )
        ).aggregate(avg_response_time=models.Avg('response_time'))['avg_response_time']
        return round(response_times.total_seconds() / 3600, 2) if response_times else 0

    def calculate_fulfilment_rate(self):
        completed_orders = self.purchaseorder_set.filter(status='completed')
        successful_fulfillments = completed_orders.filter(quality_rating__isnull=True).count()
        fulfilment_rate = (successful_fulfillments / completed_orders.count()) * 100 if completed_orders.count() > 0 else 0
        return round(fulfilment_rate, 2)


class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50, unique=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    expected_delivery_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"PO {self.po_number} - {self.vendor.name}"

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()
    
    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
