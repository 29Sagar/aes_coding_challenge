from rest_framework import serializers
from .models import Transaction, TransactionLineItem, InventoryItem, CompanyLedgerMaster, BranchMaster, DepartmentMaster, ArticleMaster, ColorMaster


class TransactionListSerialzier(serializers.ModelSerializer):
    company_name = serializers.CharField(
        source='company.name', allow_null=True)
    branch_name = serializers.CharField(
        source='branch.short_name', allow_null=True)
    department_name = serializers.CharField(
        source='department.name', allow_null=True)

    class Meta:
        model = Transaction
        fields = [
            'id',
            'company_name',
            'branch_name',
            'department_name',
            'transaction_no',
            'status',
            'remarks',
        ]


class TransactionCreateListSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class TransactionLineItemListSerialzier(serializers.ModelSerializer):
    class Meta:
        model = TransactionLineItem
        fields = '__all__'


class InventoryItemListSerialzier(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'
