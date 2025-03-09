import graphene
from graphene_django import DjangoObjectType

from django_indexer_web_app.models import Block

class BlockType(DjangoObjectType):
    class Meta:
        model = Block
        field = ("chain_id", "block_hash", "tx_num", "created_at", "height")

class Query(graphene.ObjectType):
    all_blocks = graphene.List(BlockType)

    def resolve_all_blocks(self, info):
        return Block.objects.all()
    
schema = graphene.Schema(query=Query)