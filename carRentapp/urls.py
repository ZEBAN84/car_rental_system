from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('owner_register/',views.owner_register),
    path('buyer_reg/',views.buyer_reg),
    path('driver_reg/',views.driver_reg),
    path('login/',views.login),
    path('logout/',views.logout),

    #Admin
    path('admin_home/',views.admin_home),
    path('admin_ownerlist/',views.admin_ownerlist),
    path('admin_buyerlist/',views.admin_buyerlist),
    path('admin_driverlist/',views.admin_driverlist),
    path('admin_owner_approve/',views.admin_owner_approve),
    path('admin_owner_reject/',views.admin_owner_reject),
    path('admin_driver_approve/',views.admin_driver_approve),
    path('admin_driver_reject/',views.admin_driver_reject),
    path('admin_add_police/',views.admin_add_police),
    path('admin_policelist/',views.admin_policelist),
    path('admin_feedback/',views.admin_feedback),
    path('admin_delete_feedback/',views.admin_delete_feedback),
    path('admin_view_products/',views.admin_view_products),
    path('view_paymentdetails/', views.view_paymentdetails),
    #Owner
    path('owner_home/',views.owner_home),
    path('owner_profile/',views.owner_profile),
    path('owner_edit_profile/',views.owner_edit_profile),
    path('owner_add_product/',views.owner_add_product),
    path('owner_view_product/',views.owner_view_product),
    path('owner_edit_product/',views.owner_edit_product),
    path('owner_feedback/',views.owner_feedback),
    path('owner_view_request/',views.owner_view_request),
    path('owner_approve_request/',views.owner_approve_request),
    path('owner_reject_request/',views.owner_reject_request),
    path('car_payment_view/',views.car_payment_view),
    path('owner_del_product/',views.owner_del_product),
  

    #Buyer
    path('buyer_home/',views.buyer_home),
    path('buyer_profile/',views.buyer_profile),
    path('buyer_edit_prof/',views.buyer_edit_prof),
    # path('buyer_view_product/',views.buyer_view_product),
    path('buyer_feedback/',views.buyer_feedback),
    path('buyer_request_product/',views.buyer_request_product),
    path('buyer_request_status/',views.buyer_request_status),
    path('buyer_view_driver/',views.buyer_view_driver),
    path('buyer_view_police/',views.buyer_view_police),
    path('buyer_driver_request/',views.buyer_driver_request),
    path('buyer_driver_req_status/',views.buyer_driver_req_status),
    path('buyer_complaints/',views.buyer_complaints),
    path('buyer_complaint_status/',views.buyer_complaint_status),
    path('buyer_driver_payment/', views.buyer_driver_payment),
    path('buyer_car_payment/', views.buyer_car_payment),
    # path('buyer_chekout/',views.buyer_chekout),
    path('buyer_product_review/',views.buyer_product_review),

    #Driver
    path('driver_home/',views.driver_home),
    path('driver_profile/',views.driver_profile),
    path('driver_edit_prof/',views.driver_edit_prof),
    path('driver_view_req/',views.driver_view_req),
    path('driver_approve_request/',views.driver_approve_request),
    path('driver_reject_request/',views.driver_reject_request),
    path('driver_price/',views.driver_price),
    path('payment_status/', views.payment_status),


    #Police
    path('police_home/',views.police_home),
    path('police_profile/',views.police_profile),
    path('police_edit_prof/',views.police_edit_prof),
    path('police_view_complaint/',views.police_view_complaint),
    path('police_reply/',views.police_reply),
    path('police_remove_complaint/',views.police_remove_complaint),
    





   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
