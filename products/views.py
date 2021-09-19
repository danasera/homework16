

from rest_framework import viewsets
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated

from products.models import Products
from products.permissions import IsAuthorOrIsAdmin
from products.serializers import CreateProductsSerializer, ProductsDetailSerializer, ProductsListSerializer


class ProductsListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsListSerializer


class ProductsDetailView(RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsDetailSerializer
    # lookup_url_kwarg = 'id'


class CreatePublicationView(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializer


class UpdatePublicationView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializer


class DeletePublicationView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializer



class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = CreateProductsSerializer
    permission_classes = [IsAuthorOrIsAdmin, ]


    def get_serializer_class(self):
        if self.action == 'list':
            return ProductsListSerializer
        elif self.action == 'retrieve':
            return ProductsDetailSerializer
        return CreateProductsSerializer

