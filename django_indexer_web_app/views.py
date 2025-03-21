from django.shortcuts import render
from django.http import HttpResponse
from .models import Block, Transaction
# Create your views here.
def index_page(request):
    return render(request, 'index.html',)

def blocks_page(request):
    blocks = Block.objects.all()
    return render(request, 'blocks.html', {'blocks': blocks})

def transactions_page(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions.html', {'transactions': transactions})