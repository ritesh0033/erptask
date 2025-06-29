from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from product.models import UoM, Product, ProductUoM
from .serializers import UoMSerializer, ProductSerializer, ProductUoMSerializer


# --- UoM Views ---

class UoMListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        uoms = UoM.objects.all()
        serializer = UoMSerializer(uoms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UoMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UoMDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return UoM.objects.get(pk=pk)
        except UoM.DoesNotExist:
            return None

    def get(self, request, pk):
        uom = self.get_object(pk)
        if not uom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UoMSerializer(uom)
        return Response(serializer.data)

    def put(self, request, pk):
        uom = self.get_object(pk)
        if not uom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = UoMSerializer(uom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        uom = self.get_object(pk)
        if not uom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        uom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- Product Views ---

class ProductListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        products = Product.objects.filter(organization=request.user.organization)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Product.objects.get(pk=pk, organization=user.organization)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk, request.user)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk, request.user)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.organization)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk, request.user)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# --- ProductUoM Views ---

class ProductUoMListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        product_uoms = ProductUoM.objects.all()
        serializer = ProductUoMSerializer(product_uoms, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductUoMSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUoMDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return ProductUoM.objects.get(pk=pk)
        except ProductUoM.DoesNotExist:
            return None

    def get(self, request, pk):
        product_uom = self.get_object(pk)
        if not product_uom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductUoMSerializer(product_uom)
        return Response(serializer.data)

    def put(self, request, pk):
        product_uom = self.get_object(pk)
        if not product_uom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductUoMSerializer(product_uom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product_uom = self.get_object(pk)
        if not product_uom:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product_uom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
