from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from inventory.models import Warehouse, InventoryLocation, InventoryItem, InventoryTransaction
from .serializers import (
    WarehouseSerializer,
    InventoryLocationSerializer,
    InventoryItemSerializer,
    InventoryTransactionSerializer,
)


# Warehouse 

class WarehouseListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        warehouses = Warehouse.objects.filter(organization=request.user.organization)
        serializer = WarehouseSerializer(warehouses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Warehouse.objects.get(pk=pk, organization=user.organization)
        except Warehouse.DoesNotExist:
            return None

    def get(self, request, pk):
        warehouse = self.get_object(pk, request.user)
        if not warehouse:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WarehouseSerializer(warehouse)
        return Response(serializer.data)

    def put(self, request, pk):
        warehouse = self.get_object(pk, request.user)
        if not warehouse:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = WarehouseSerializer(warehouse, data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        warehouse = self.get_object(pk, request.user)
        if not warehouse:
            return Response(status=status.HTTP_404_NOT_FOUND)
        warehouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# InventoryLocation 

class InventoryLocationListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        locations = InventoryLocation.objects.filter(organization=request.user.organization)
        serializer = InventoryLocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryLocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryLocationDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return InventoryLocation.objects.get(pk=pk, organization=user.organization)
        except InventoryLocation.DoesNotExist:
            return None

    def get(self, request, pk):
        location = self.get_object(pk, request.user)
        if not location:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventoryLocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, pk):
        location = self.get_object(pk, request.user)
        if not location:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventoryLocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        location = self.get_object(pk, request.user)
        if not location:
            return Response(status=status.HTTP_404_NOT_FOUND)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# InventoryItem

class InventoryItemListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        items = InventoryItem.objects.filter(organization=request.user.organization)
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryItemDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return InventoryItem.objects.get(pk=pk, organization=user.organization)
        except InventoryItem.DoesNotExist:
            return None

    def get(self, request, pk):
        item = self.get_object(pk, request.user)
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventoryItemSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk, request.user)
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventoryItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk, request.user)
        if not item:
            return Response(status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- InventoryTransaction ---

class InventoryTransactionListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        transactions = InventoryTransaction.objects.filter(organization=request.user.organization)
        serializer = InventoryTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryTransactionDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return InventoryTransaction.objects.get(pk=pk, organization=user.organization)
        except InventoryTransaction.DoesNotExist:
            return None

    def get(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventoryTransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = InventoryTransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = self.get_object(pk, request.user)
        if not transaction:
            return Response(status=status.HTTP_404_NOT_FOUND)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
