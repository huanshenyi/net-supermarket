from rest_framework import serializers

from .models import Goods, GoodsCategory


# モデル関連
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializers(serializers.ModelSerializer):
    # name = serializers.CharField(required=True, max_length=100)
    # click_num = serializers.IntegerField(default=0)
    # goods_front_image = serializers.CharField(required=True)
    category = CategorySerializer()
    class Meta:
        model = Goods
        # fields = ('name', 'click_num', 'market_price', 'add_time')
        fields = "__all__"

    # def create(self, validated_data):
    #     return Goods.objects.create(**validated_data)