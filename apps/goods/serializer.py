from rest_framework import serializers


class GoodsSerializers(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.CharField(required=True)