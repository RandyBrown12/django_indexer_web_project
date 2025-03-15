from django.db import models

# Create your models here.
class Block(models.Model):
    block_id = models.UUIDField(primary_key=True)
    block_hash = models.CharField(null=False)
    chain_id = models.CharField(null=False)
    created_at = models.DateTimeField(null=False)
    height = models.IntegerField(null=False)
    tx_num = models.IntegerField(null=False)

    class Meta:
        managed = False
        db_table = 'blocks'

class Transaction(models.Model):
    tx_id = models.UUIDField(primary_key=True)
    tx_hash = models.CharField(null=False)
    height = models.CharField(null=False)
    fee_amount = models.CharField(null=False)
    fee_denom = models.CharField(null=False)
    created_at = models.DateTimeField(null=False)

    class Meta:
        managed = False
        db_table = 'transactions'