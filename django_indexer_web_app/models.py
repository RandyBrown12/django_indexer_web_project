from django.db import models
import sys

# Check if python is in testing mode:
IN_TEST_STAGE = 'test' in sys.argv

# Create your models here.
class Block(models.Model):
    block_id = models.UUIDField(primary_key=True)
    block_hash = models.CharField(null=False)
    chain_id = models.CharField(null=False)
    created_at = models.DateTimeField(null=False)
    height = models.IntegerField(null=False)
    tx_num = models.IntegerField(null=False)

    class Meta:
        managed = IN_TEST_STAGE
        db_table = 'blocks'

class Transaction(models.Model):
    tx_id = models.UUIDField(primary_key=True)
    block_id = models.ForeignKey(Block, on_delete=models.CASCADE, db_column='block_id')
    tx_hash = models.CharField(null=False)
    height = models.CharField(null=False)
    fee_amount = models.CharField(null=False)
    fee_denom = models.CharField(null=False)
    created_at = models.DateTimeField(null=False)

    class Meta:
        managed = IN_TEST_STAGE
        db_table = 'transactions'