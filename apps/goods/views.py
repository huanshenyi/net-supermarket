from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Goods
from .serializer import GoodsSerializers


class GoodsListView(APIView):
    def get(self, request, format=None):
        goods = Goods.objects.all()
        goods_serializer = GoodsSerializers(goods, many=True)
        return Response(goods_serializer.data)

