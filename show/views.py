from django.shortcuts import render
from django.http import HttpResponse
from management.models import warehouse, good, StoW, storekeeper


# Create your views here.
def show(req):
    if req.method == 'POST':
        pass
    elif req.method == 'GET':
        warehouses = warehouse.objects.all()
        goods = good.objects.all()
        storekeepers = storekeeper.objects.all()
        return render(req, 'show/show.html', locals())


def detail(req, obj, _id):
    elementId = _id
    if req.method == 'POST':
        pass
    elif req.method == 'GET':
        if obj == 'warehouse':
            warehouse_obj = warehouse.objects.get(id=_id)
            # 1
            goods = good.objects.filter(warehouse_id=_id)
            # 2
            # goods = warehouse_obj.warehouse_set.all()

            ids = StoW.objects.filter(warehouse_id=_id)
            Ids = []
            for sid in ids:
                Ids.append(sid.storekeeper_id)
            storekeepers = storekeeper.objects.filter(id__in=Ids)

            # null检查,此处忽略
            return render(req, 'show/show_detail.html', locals())
        elif obj == 'storekeeper':
            storekeeper_obj = storekeeper.objects.get(id=_id)
            ids = StoW.objects.filter(storekeeper_id=_id)
            Ids = []
            for sid in ids:
                Ids.append(sid.warehouse_id)
            warehouses = warehouse.objects.filter(id__in=Ids)
            return render(req, 'show/show_detail.html', locals())
        elif obj == 'good':
            pass
