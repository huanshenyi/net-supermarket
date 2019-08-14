from rest_framework import serializers

from .models import Goods, GoodsCategory, GoodsImage


# モデル関連
class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image",)

class GoodsSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.CharField(required=True)
    category = CategorySerializer()
    images = GoodsImagesSerializer(many=True)
    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"

    # def create(self, validated_data):
    #     return Goods.objects.create(**validated_data)