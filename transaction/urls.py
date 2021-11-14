from django.urls import path
from transaction import views

transaction_urls = [
    path('', views.TransactionListCreateAPIView.as_view(),
         name='transaction-create-list'),
    path('transactionItem/', views.TransactionItemListCreateAPIView.as_view(),
         name='transactionItem-create-list'),
    path('inventoryItem/', views.InventoryItemListCreateAPIView.as_view(),
         name='inventoryItem-create-list'),
    path('<int:pk>/', views.RemoveTransactionView.as_view(),
         name='transaction-delete-list'),
    path('transactionDetail/', views.TransactionDetailView.as_view(),
         name='transaction-detail-list'),
]
