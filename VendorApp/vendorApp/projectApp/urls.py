from django.urls import path
from . import views

urlpatterns = [

    # Vendor Profile Management
    path('vendor/', views.create_vendor, name='create_vendor'), # POST Request
    path('vendors/<int:vendor_id>/', views.retrieve_vendor, name='retrieve_vendor'), #GET Specified
    path('vendors/<int:vendor_id>/update/', views.update_vendor, name='update_vendor'), # Update Specified
    path('vendors/<int:vendor_id>/delete/', views.delete_vendor, name='delete_vendor'), # Delete Specified
    path('vendors/', views.list_vendors, name='list_vendors'), # GET All

    # Purchase Order Tracking
    path('purchase_order/', views.create_purchase_order, name='create_purchase_order'),  # Post Request
    path('purchase_orders/<int:po_id>/', views.retrieve_purchase_order, name='retrieve_purchase_order'), #GET Request
    path('purchase_orders/<int:po_id>/update/', views.update_purchase_order, name='update_purchase_order'), #Update Specified
    path('purchase_orders/<int:po_id>/delete/', views.delete_purchase_order, name='delete_purchase_order'), # Delete Specified
    path('purchase_orders/', views.list_purchase_orders, name='list_purchase_orders'), # GET All

    # Vendor Performance Evaluation
    path('vendors/<int:vendor_id>/performance/', views.vendor_performance, name='vendor_performance'),
]
