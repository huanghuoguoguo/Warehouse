from django.shortcuts import render
from . import models
from .models import good, warehouse, storekeeper


def addGood(req):
    # 获取data
    # 创建对象 上传数据库
    name = req.POST.get('name')
    warehouse_id = req.POST.get('warehouse_id')
    w = warehouse.objects.get(id=warehouse_id)
    good_class = req.POST.get('good_class')
    good_info = req.POST.get('good_info')
    amount = req.POST.get('amount')

    good.objects.create(name=name, warehouse=w, good_class=good_class,
                        good_info=good_info,
                        amount=amount)


def addStorekeeper(req):
    name = req.POST.get('name')
    age = req.POST.get('age')
    sex = req.POST.get('sex')
    degree = req.POST.get('degree')
    origin = req.POST.get('origin')
    storekeeper.objects.create(name=name, age=age, sex=sex, degree=degree, origin=origin)


def addWarehouse(req):
    name = req.POST.get('name')
    capacity = req.POST.get('capacity')
    info = req.POST.get('info')
    goods_numbers = req.POST.get('goods_numbers')
    warehouse.objects.create(name=name, capacity=capacity, info=info, goods_numbers=goods_numbers)
