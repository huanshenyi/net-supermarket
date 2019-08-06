from django.views import View
from .models import Goods

class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()
        for good in goods:
            json_dict ={}
            json_dict["name"] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            # json_dict['add_time'] = good.add_time
            json_list.append(json_dict)
        from django.http import HttpResponse
        import json
        return HttpResponse(json.dumps(json_list), content_type="application/json")