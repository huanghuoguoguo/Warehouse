from django.shortcuts import render
from .addFunc import *
from .deleteFunc import *
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.apps import apps

from .models import StoW


def add(req, obj):
    if req.method == 'GET':
        return render(req, 'add/add.html', locals())
    elif req.method == 'POST':
        if obj == 'good':
            addGood(req)
        elif obj == 'storekeeper':
            addStorekeeper(req)
        elif obj == 'warehouse':
            addWarehouse(req)
        return HttpResponseRedirect('show/')


def delete(req, obj, _id):
    # return HttpResponse('this is ok2')
    if req.method == 'GET':
        if obj == 'good':
            delGood(_id)
        elif obj == 'warehouse':
            delWarehouse(_id)
        elif obj == 'storekeeper':
            delStorekeeper(_id)
        return HttpResponseRedirect('/show/')


def modify(req, obj, _id):
    obj_ = globals()[obj].objects.get(id=_id)
    # modelobj = apps.get_model('management', 'warehouse')
    #
    # field_list = []
    #
    # for field in modelobj._meta.fields:
    #     field_list.append(field.name)  # 获取英文列名
    #     field_list.append(field.verbose_name)  # 获取中文列名
    # print(field_list)
    if req.method == 'GET':
        # return render(req, 'test.html', locals())
        return render(req, 'modify/modify.html', locals())
    elif req.method == 'POST':
        if obj == 'warehouse':
            name = req.POST.get('name')
            capacity = req.POST.get('capacity')
            info = req.POST.get('info')
            goods_numbers = req.POST.get('goods_numbers')
            obj_.name = name
            obj_.capacity = capacity
            obj_.info = info
            obj_.goods_numbers = goods_numbers
        elif obj == 'storekeeper':
            name = req.POST.get('name')
            age = req.POST.get('age')
            sex = req.POST.get('sex')
            degree = req.POST.get('degree')
            origin = req.POST.get('origin')
            obj_.name = name
            obj_.age = age
            obj_.sex = sex
            obj_.degree = degree
            obj_.origin = origin

        elif obj == 'good':
            name = req.POST.get('name')
            warehouse_id = req.POST.get('warehouse_id')
            w = warehouse.objects.get(id=warehouse_id)
            good_class = req.POST.get('good_class')
            good_info = req.POST.get('good_info')
            amount = req.POST.get('amount')
            obj_.name = name
            obj_.warehouse = w
            obj_.good_class = good_class
            obj_.good_info = good_info
            obj_.amount = amount
        # 保存
        obj_.save()


def deleteStoW(req, wid, sid):
    stow = StoW.objects.filter(storekeeper_id=wid, warehouse_id=wid)
    stow.delete()
    address = '/show/detail/warehouse/' + str(wid)
    return HttpResponseRedirect(address)


def addStorekeeper(req, wh_id):
    if req.method == 'GET':
        return render(req, 'addStorekeeper/addStorekeeper.html', locals())
    elif req.method == 'POST':
        Sk_id = req.POST.get('Sk_id', '')
        wh = warehouse.objects.get(id=wh_id)
        sk = storekeeper.objects.get(id=Sk_id)
        StoW.objects.create(warehouse=wh, storekeeper=sk)
        address = '/show/detail/warehouse/' + str(wh_id)
        return HttpResponseRedirect(address)
