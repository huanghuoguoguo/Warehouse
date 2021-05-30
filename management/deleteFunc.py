from django.shortcuts import render
from . import models
from .models import good, warehouse, storekeeper


def delGood(_id):
    Good = good.objects.get(id=_id)
    Good.delete()


def delStorekeeper(_id):
    Storekeeper = storekeeper.objects.get(id=_id)
    Storekeeper.delete()


def delWarehouse(_id):
    Warehouse = warehouse.objects.get(id=_id)
    Warehouse.delete()
