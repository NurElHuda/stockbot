from rest_framework import serializers

from app_src.api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="pk", read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
        ]


# class ProductLogoSerializer(serializers.ModelSerializer):
#     logo = serializers.ImageField(max_length=5000, allow_empty_file=False, use_url=True)

#     class Meta:
#         model = Product
#         fields = ["id", "logo"]

#     def update(self, instance, validated_data):
#         instance.logo = validated_data.get("logo", None)
#         instance.save()
#         return instance
