from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import Goods
from .serializer import GoodsSerializers


class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers

    # ここのself.listはmixins.ListModelMixinにある
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)







# class GoodsListView(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializers(goods, many=True)
#         return Response(goods_serializer.data)
#
#     def post(self, request):
#         # request.data = 普通のdjangoのrequestのパッケージ化
#         serializer = GoodsSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

