from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/',views.index, name='dashboard-index'),
    path('staff/',views.staff, name='dashboard-staff'),
    path('staff_detail/<int:pk>',views.staff_detail, name='dashboard-staff-detail'),
    path('staff_index/',views.staff_index, name='dashboard-staff-index'),
    path('product/',views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/',views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/',views.product_update, name='dashboard-product-update'),
    path('order/',views.order, name='dashboard-order'),
]

