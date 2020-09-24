from django.db import models
from django.contrib.auth.models import User

from mdeditor.fields import MDTextField

# from rbac.models import UserInfo as RbacUserInfo


# Create your models here.
class Supplier(models.Model):  # 供应商
    name = models.CharField(max_length=64, verbose_name='供应商', unique=True)
    tel = models.CharField(max_length=256, verbose_name='优势品牌', blank=True, null=True)
    contact = models.CharField(max_length=64, verbose_name='联系人', blank=True, null=True)
    phone = models.CharField(max_length=13, verbose_name='联系手机', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'


class Brand(models.Model):
    name = models.CharField(max_length=24, verbose_name='品牌')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class Goods(models.Model):  # 货品资料
    brand = models.ForeignKey(to='Brand', verbose_name='品牌', on_delete=models.CASCADE)
    Gmodel = models.CharField(max_length=64, unique=True, verbose_name='品名规格')
    unit_choices = (
        (0, '台'),
        (1, '支'),
        (2, '个'),
        (3, '站点'),
        (4, '用户'),
        (5, '套'),
        (6, '平方'),
        (7, '卷'),
        (8, '根'),
        (9, 'PCS'),
    )
    unit = models.IntegerField(choices=unit_choices, verbose_name='单位', default=0, )
    type_choices = (
        (0, '条码打印机'),
        (1, '条码扫描器'),
        (2, '数据终端'),
        (3, '软件'),
        (4, '配件'),
        (5, '耗材'),
        (6, 'RFID设备'),
        (7, '其它'),
    )
    type = models.IntegerField(choices=type_choices, verbose_name='分类', default=0, )

    # attribute = models.CharField(max_length=64, verbose_name='属性', blank=True, null=True)
    price = models.FloatField(verbose_name='产品进价', default=0)
    min_price = models.FloatField(verbose_name='最低售价', default=0)
    meno = models.CharField(verbose_name='备注', default='', blank=True, null=True,max_length=128)
    supplier = models.ForeignKey(to='Supplier', verbose_name='供应商', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='操作员', on_delete=models.CASCADE, editable=False, null=True)

    date = models.DateField(verbose_name='更改日期', auto_now=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品信息'

    def __str__(self):
        return self.Gmodel


# class Unit(models.Model):  # 货品单位
#     name = models.CharField(max_length=24, verbose_name='单位')
#
#     def __str__(self):
#         return self.name


# class Type(models.Model):  # 货品类别
#     name = models.CharField(max_length=24, verbose_name='货品分类')
#
#     def __str__(self):
#         return self.name
# class UserInfo(RbacUserInfo):
#     nickname = models.CharField(verbose_name='姓名',max_length=32)
#     phone = models.CharField(verbose_name='手机',max_length=16)
#
#     def __str__(self):
#         return self.nickname

class Knowledge(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题', blank=True, null=True)
    details = MDTextField(verbose_name='详情')
    user = models.ForeignKey(User, verbose_name='操作员', on_delete=models.CASCADE, editable=False, null=True)

    date = models.DateField(verbose_name='更改日期', auto_now=True)

    class Meta:
        verbose_name = '经验'
        verbose_name_plural = '经验'

    def __str__(self):
        return self.title


class Model_record(models.Model):
    sk_model = models.CharField(max_length=32, verbose_name='公司型号')
    sp_model = models.CharField(max_length=32, verbose_name='供应商型号')
    supplier = models.ForeignKey(Supplier, verbose_name='供应商', on_delete=models.CASCADE)
    meno = models.CharField(max_length=128, verbose_name='备注', blank=True, null=True)

    def __str__(self):
        return self.sk_model

    class Meta:
        verbose_name = '型号登记'
        verbose_name_plural = '型号登记'
