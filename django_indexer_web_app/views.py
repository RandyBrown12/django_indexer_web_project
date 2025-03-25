from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Block, Transaction

# Create your views here.
def home_page(request):
    return render(request, 'index.html',)

def blocks_page(request):
    max_blocks = 50
    blocks = Block.objects.order_by("-created_at")
    paginator = Paginator(blocks, max_blocks)

    blocks_page_number = request.GET.get("page")
    page_blocks = paginator.get_page(blocks_page_number)
    return render(request, 'blocks.html', {'blocks': page_blocks, 'block_page_count': paginator.num_pages, 'block_page_current': page_blocks.number, 'block_page_view_range': range(page_blocks.number - 1, page_blocks.number + 2)})

def transactions_page(request):
    max_transactions = 50
    transactions = Transaction.objects.order_by("-created_at")
    paginator = Paginator(transactions, max_transactions)

    transactions_page_number = request.GET.get("page")
    transactions_blocks = paginator.get_page(transactions_page_number)
    print(paginator.num_pages)
    return render(request, 'transactions.html', {'transactions': transactions_blocks})