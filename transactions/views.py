# transactions/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination


class TransactionPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 20


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ["description"]  # added line for searching by description
    pagination_class = TransactionPagination

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
