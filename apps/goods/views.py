from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters

from .models import Goods, GoodsCategory
from .serializer import GoodsSerializers, CategorySerializer
from .filters import GoodsFilter


class GoodsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# generics.ListAPIView = mixins.ListModelMixin,GenericAPIView　の継承
class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = GoodsSetPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    # https://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')

    # (mixins.ListModelMixin)
    # ここのself.listはmixins.ListModelMixinにある
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
    商品分類リストデータ
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer







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

