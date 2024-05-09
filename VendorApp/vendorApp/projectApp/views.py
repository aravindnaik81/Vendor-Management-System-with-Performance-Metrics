from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformanceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Vendor Profile Management

# Post New Vendors ------->
@api_view(['POST'])
def create_vendor(request):
    serializer = VendorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message": "Vendor created successfully", "Vendor": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"Message": "Failed to create vendor", "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Get All Vendors ------->
@api_view(['GET'])
def list_vendors(request):
    vendors = Vendor.objects.all()
    serializer = VendorSerializer(vendors, many=True)
    return Response({"Message": " All Successfull Vendors ", "Vendor": serializer.data})

# Get Specified Vendor ------>
@api_view(['GET'])
def retrieve_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    serializer = VendorSerializer(vendor)
    return Response({"Message": "Vendor retrieved successfully", "Vendor": serializer.data})

# Update Vendor -------->
@api_view(['PUT'])
def update_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    serializer = VendorSerializer(vendor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message": "Vendor updated successfully", "Vendor": serializer.data})
    return Response({"Message": "Failed to update vendor", "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Delete Vendor -------->
@api_view(['DELETE'])
def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    vendor.delete()
    return Response({"Message": "Vendor deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Purchase Order Tracking

# Create(POST) New Purchase --------->
@api_view(['POST'])
def create_purchase_order(request):
    serializer = PurchaseOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message": "Purchase order created successfully", "PurchaseOrder": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"Message": "Failed to create purchase order", "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# GET all saved Orders ------>
@api_view(['GET'])
def list_purchase_orders(request):
    purchase_orders = PurchaseOrder.objects.all()
    serializer = PurchaseOrderSerializer(purchase_orders, many=True)
    return Response({"Message": "All Orders Purchased ", "PurchaseOrder": serializer.data})

#GET Specified Purchase ------->
@api_view(['GET'])
def retrieve_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
    serializer = PurchaseOrderSerializer(purchase_order)
    return Response({"Message": "Purchase order retrieved successfully", "PurchaseOrder": serializer.data})

# Update(PUT) existing order ------>
@api_view(['PUT'])
def update_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
    serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message": "Purchase order updated successfully", "PurchaseOrder": serializer.data})
    return Response({"Message": "Failed to update purchase order", "Errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Delete Soecified Order ------>
@api_view(['DELETE'])
def delete_purchase_order(request, po_id):
    purchase_order = get_object_or_404(PurchaseOrder, pk=po_id)
    purchase_order.delete()
    return Response({"Message": "Purchase order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


# Vendor Performance Evaluation
@api_view(['GET'])
def vendor_performance(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)
    serializer = VendorPerformanceSerializer(vendor)
    return Response({"Message": "Vendor performance data retrieved successfully", "PerformanceData": serializer.data})
