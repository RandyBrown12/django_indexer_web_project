from django.db import models

# Create your models here.
class Block(models.Model):
    block_hash = models.CharField(null=False)
    chain_id = models.CharField(null=False)
    created_at = models.DateTimeField(null=False)
    height = models.IntegerField(null=False, primary_key=True)
    tx_num = models.IntegerField(null=False)

    class Meta:
        managed = False
        db_table = 'blocks'
        unique_together = (('chain_id', 'height'), ('chain_id', 'block_hash', 'height'),)