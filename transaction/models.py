from django.db import models
from .utils import *


# Masters required in transaction models
class BranchMaster(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    contact_person_name = models.CharField(max_length=20)
    gst_number = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.short_name


class DepartmentMaster(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class CompanyLedgerMaster(models.Model):
    name = models.CharField(max_length=32, unique=True)
    gst_number = models.CharField(max_length=20, unique=True)
    supplier_status = models.BooleanField(default=False)
    address1 = models.CharField(max_length=50)
    pin_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    remarks = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class ArticleMaster(models.Model):
    name = models.CharField(max_length=80, unique=True)
    short_name = models.CharField(max_length=50, unique=True)
    blend_pct = models.CharField(max_length=50)
    twists = models.PositiveIntegerField(blank=True, null=True)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name


class ColorMaster(models.Model):
    article = models.ForeignKey(ArticleMaster, on_delete=models.PROTECT)
    name = models.CharField(max_length=20)
    short_name = models.CharField(max_length=20)
    remarks = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.name

# Create your models here.


class Transaction(models.Model):
    class status_choice(models.TextChoices):
        PENDING = 'PENDING'
        COMPLETED = 'COMPLETED'
        CLOSE = 'CLOSE'

    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchMaster, on_delete=models.CASCADE)
    department = models.ForeignKey(
        DepartmentMaster, on_delete=models.CASCADE)
    transaction_no = models.CharField(max_length=20,
                                      blank=True,
                                      editable=False,
                                      unique=True,
                                      default=create_new_tr_number())
    status = models.CharField(choices=status_choice.choices,
                              max_length=30)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.transaction_no


class TransactionLineItem(models.Model):
    class unit_choice(models.TextChoices):
        KG = 'KG'
        METRE = 'METRE'

    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    transaction = models.ForeignKey(
        Transaction, on_delete=models.CASCADE, null=True, blank=True)
    required_at = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField(null=True, blank=True)
    rate_per_unit = models.IntegerField(null=True, blank=True)
    unit = models.CharField(choices=unit_choice.choices,
                            max_length=30)


class InventoryItem(models.Model):
    class unit_choice(models.TextChoices):
        KG = 'KG'
        METRE = 'METRE'

    article = models.ForeignKey(ArticleMaster, on_delete=models.CASCADE)
    colour = models.ForeignKey(ColorMaster, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyLedgerMaster, on_delete=models.CASCADE)
    transaction_line_item = models.ForeignKey(
        TransactionLineItem, on_delete=models.CASCADE, null=True, blank=True)
    gross_quantity = models.FloatField(null=True, blank=True)
    net_quantity = models.FloatField(null=True, blank=True)
    unit = models.CharField(choices=unit_choice.choices,
                            max_length=30)
