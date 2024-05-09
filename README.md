# Vendor Management System
 Description:-
   The Vendor Management System is a Django application developed to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

Features:-
Vendor Profile Management:
Create, retrieve, update, and delete vendor profiles.

Purchase Order Tracking:
Create, retrieve, update, and delete purchase orders.

Vendor Performance Evaluation:
Calculate performance metrics such as on-time delivery rate, quality rating, response time, and fulfilment rate.

API Endpoints:-
# Vendor Profile Management
path('vendor/', views.create_vendor, name='create_vendor'): Create a  new Vendor
path('vendors/<int:vendor_id>/', views.retrieve_vendor, name='retrieve_vendor'): Retrieve a Specific vendor
path('vendors/<int:vendor_id>/update/', views.update_vendor, name='update_vendor'): Update a vendor
path('vendors/<int:vendor_id>/delete/', views.delete_vendor, name='delete_vendor'): Delete a vendor
path('vendors/', views.list_vendors, name='list_vendors'): Retrives all Vendors

# Purchase Order Tracking
purchase_order/ : Create a newpurchase order
purchase_orders/<int:po_id>/ : Retrieves a specified purchase order
purchase_orders/<int:po_id>/update/ : Update a purchase order
purchase_orders/<int:po_id>/delete/ : Delete a purchase order
purchase_orders/ : Retrieves all purchased order

# Vendor Performance Evaluation
vendors/<int:vendor_id>/performance/ : Retrieve performance metrics for a vendor.

Contributors:
Aravind Naik Ramavath

I did this project and this is an assessment. I received from linkedin send by karan grover Co-Founder at Fatmug.
