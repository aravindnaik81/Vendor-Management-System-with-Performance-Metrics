# vendors/serializers.py
from rest_framework import serializers
from .models import *


# Vendor Serializer -------->
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


# Purchase Order Tracing ------->
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

# Vendor Performance Serializer ------->
from rest_framework import serializers
from .models import Vendor

class VendorPerformanceSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.SerializerMethodField()
    quality_rating_average = serializers.SerializerMethodField()
    average_response_time = serializers.SerializerMethodField()
    fulfilment_rate = serializers.SerializerMethodField()

    class Meta:
        model = Vendor
        fields = ('on_time_delivery_rate', 'quality_rating_average', 'average_response_time', 'fulfilment_rate')

    def get_on_time_delivery_rate(self, obj):
        return obj.calculate_on_time_delivery_rate()

    def get_quality_rating_average(self, obj):
        return obj.calculate_quality_rating_average()

    def get_average_response_time(self, obj):
        return obj.calculate_average_response_time()

    def get_fulfilment_rate(self, obj):
        return obj.calculate_fulfilment_rate()

