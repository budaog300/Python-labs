from django.urls import path

from .views import (
    IndexView,
    item_list, item_update, item_delete,
    cashier_list, cashier_update, cashier_delete,
    store_list, store_update, store_delete,
    check_list, check_update, check_delete,
    sale_list, sale_update, sale_delete,
    register,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('patients/', item_list, name='item_list'),
    path('patients/<int:pk>/update', item_update, name='item_update'),
    path('patients/<int:pk>/delete', item_delete, name='item_delete'),

    path('doctors/', cashier_list, name='cashier_list'),
    path('doctors/<int:pk>/update', cashier_update, name='cashier_update'),
    path('doctors/<int:pk>/delete', cashier_delete, name='cashier_delete'),

    path('hospitals/', store_list, name='store_list'),
    path('hospitals/<int:pk>/update',store_update, name='store_update'),
    path('hospitals/<int:pk>/delete', store_delete, name='store_delete'),

    path('reason/', check_list, name='check_list'),
    path('reason/<int:pk>/update', check_update, name='check_update'),
    path('reason/<int:pk>/delete', check_delete, name='check_delete'),
    
    path('duration/', sale_list, name='sale_list'),
    path('duration/<int:pk>/sales', sale_update, name='sale_update'),
    path('duration/<int:pk>/delete', sale_delete, name='sale_delete'),

    path('register/', register, name='register'),
    
]
