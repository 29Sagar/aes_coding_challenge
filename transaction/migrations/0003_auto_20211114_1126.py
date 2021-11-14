# Generated by Django 3.1.1 on 2021-11-14 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_inventoryitem_transaction_transactionlineitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='transaction_line_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.transactionlineitem'),
        ),
        migrations.AddField(
            model_name='transactionlineitem',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='transaction.transaction'),
        ),
    ]
