from django.contrib import admin
from transaction.models import BranchMaster, DepartmentMaster, CompanyLedgerMaster, ArticleMaster, ColorMaster, Transaction, TransactionLineItem, InventoryItem

# Register your models here.
admin.site.register(BranchMaster)
admin.site.register(DepartmentMaster)
admin.site.register(CompanyLedgerMaster)
admin.site.register(ArticleMaster)
admin.site.register(ColorMaster)


admin.site.register(Transaction)
admin.site.register(TransactionLineItem)
admin.site.register(InventoryItem)
