from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
    RetrieveUpdateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from transaction.serializer import TransactionListSerialzier, TransactionLineItemListSerialzier, InventoryItemListSerialzier,\
    TransactionCreateListSerialzier
from .models import Transaction, TransactionLineItem, InventoryItem
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.


class TransactionListCreateAPIView(ListCreateAPIView):
    parser_classes = [FormParser, JSONParser, MultiPartParser]
    # serializer_class = TransactionListSerialzier

    def get_serializer_class(self):
        switcher = {
            'GET': TransactionListSerialzier,
            'POST': TransactionCreateListSerialzier,

        }
        return switcher[self.request.method]

    def get_queryset(self):
        queryset = Transaction.objects.all()
        return queryset


class TransactionItemListCreateAPIView(ListCreateAPIView):
    parser_classes = [FormParser, JSONParser, MultiPartParser]
    # serializer_class = TransactionLineItemListSerialzier

    def get_serializer_class(self):
        switcher = {
            'GET': TransactionLineItemListSerialzier,
            'POST': TransactionLineItemListSerialzier,

        }
        return switcher[self.request.method]

    def get_queryset(self):
        queryset = TransactionLineItem.objects.all()
        return queryset


class InventoryItemListCreateAPIView(ListCreateAPIView):
    parser_classes = [FormParser, JSONParser, MultiPartParser]
    # serializer_class = TransactionLineItemListSerialzier

    def get_serializer_class(self):
        switcher = {
            'GET': InventoryItemListSerialzier,
            'POST': InventoryItemListSerialzier,

        }
        return switcher[self.request.method]

    def get_queryset(self):
        queryset = InventoryItem.objects.all()
        return queryset


class RemoveTransactionView(RetrieveUpdateDestroyAPIView):
    """
    Query Parmeter
    --------------------------------------------------
    transaction_id : integer
    --------------------------------------------------
    e.g. http://127.0.0.1:8000/transaction/1
    """

    queryset = Transaction.objects.none()

    def get_serializer_class(self):
        switcher = {
            'GET': TransactionListSerialzier,
            'PUT': TransactionListSerialzier,
            'PATCH': TransactionListSerialzier,

        }
        return switcher[self.request.method]

    def get_queryset(self):
        obj = Transaction.objects.filter(id=self.kwargs['pk'])
        return obj

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(self.get_queryset())
        transaction_line_data = TransactionLineItem.objects.filter(
            transaction_id=instance.id).first()
        if transaction_line_data:
            inventory_data = InventoryItem.objects.filter(
                transaction_line_item_id=transaction_line_data.id)
        else:
            inventory_data = False
        if inventory_data:
            response = Response(status=status.HTTP_204_NO_CONTENT,
                                data={'message': "Transaction can't be deleted beacause inventory is created"})
        else:
            instance.delete()
            response = Response(status=status.HTTP_204_NO_CONTENT,
                                data={'message': 'Transaction Deleted Successfully.'})
        return response


class TransactionDetailView(GenericAPIView):
    queryset = Transaction.objects.none()

    def get(self, request, *args, **kwargs):
        transaction_data = Transaction.objects.all()
        data = []
        data1 = []
        for t_data in transaction_data:
            id = t_data.id
            transaction_no = t_data.transaction_no
            status = t_data.status
            remarks = t_data.remarks
            line_items_data = TransactionLineItem.objects.filter(
                transaction_id=id)
            if line_items_data:
                data1 = []
                for items in line_items_data:
                    required_at = items.required_at
                    quantity = items.quantity
                    rate_per_unit = items.rate_per_unit
                    unit = items.unit
                    line_items_data = {
                        'required_at': required_at,
                        'quantity': quantity,
                        'rate_per_unit': rate_per_unit,
                        'unit': unit,
                    }
                    data1.append(line_items_data)

            result = {
                'id': id,
                'transaction_no': transaction_no,
                'status': status,
                'remarks': remarks,
                'line_items_data': data1,
            }
            data.append(result)

        return Response(data)
