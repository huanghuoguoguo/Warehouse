from django.db import models


# Create your models here.
class warehouse(models.Model):
    name = models.CharField('名称', max_length=10)
    capacity = models.PositiveIntegerField('容量')
    createTime = models.DateTimeField('创建时间', auto_now_add=True)
    info = models.TextField('仓库信息')
    goods_numbers = models.PositiveIntegerField('物品数')

    class Meta:
        db_table = 'warehouse'


class good(models.Model):
    name = models.CharField('名称', max_length=10)
    warehouse = models.ForeignKey(warehouse, on_delete=models.SET_NULL, null=True)
    good_class = models.CharField('类别', max_length=10)
    good_info = models.TextField('货物信息')
    create_time = models.DateTimeField('入库时间', auto_now_add=True)
    amount = models.PositiveIntegerField('剩余量')

    class Meta:
        db_table = 'goods'


class storekeeper(models.Model):
    name = models.CharField('姓名', max_length=5)
    age = models.SmallIntegerField('年龄')
    sex = models.BooleanField('性别')
    degree = models.CharField('学历', max_length=10)
    origin = models.CharField('籍贯', max_length=10)
    onJobTime = models.DateTimeField('入职时间', auto_now_add=True)

    class Meta:
        db_table = 'storekeeper'


class StoW(models.Model):
    # 在mysql中需要创建第三张表，orm体系下可以使用manytomany自动创建，但是本个项目中并不指定
    storekeeper = models.ForeignKey('storekeeper', on_delete=models.CASCADE)
    warehouse = models.ForeignKey('warehouse', on_delete=models.CASCADE)

    class Meta:
        db_table = 'StoW'
