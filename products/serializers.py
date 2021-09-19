from rest_framework import serializers

from products.models import Products


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class ProductsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CreateProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        exclude = ('user', )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        return super().create(validated_data)