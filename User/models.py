from django.db import models


class Administrator(models.Model):
    username = models.CharField(max_length=32, default='')
    password = models.CharField(max_length=32, default='')


class User(models.Model):
    username = models.CharField(max_length=32, default='')
    password = models.CharField(max_length=32, default='')
    telephone = models.CharField(max_length=32, default='')
    identity = models.CharField(max_length=32, default='')
    province = models.CharField(max_length=32, default='')
    area = models.IntegerField(default=0)
    species = models.CharField(max_length=32, default='')


class Shops(models.Model):
    username = models.CharField(max_length=32, default='')
    password = models.CharField(max_length=32, default='')
    telephone = models.CharField(max_length=32, default='')
    identity = models.CharField(max_length=32, default='')


class Recommend(models.Model):
    rid = models.IntegerField(default=0)
    name = models.CharField(max_length=32, default='')
    imgUrl = models.CharField(max_length=256, default='')
    detailUrl = models.CharField(max_length=2048, default='')


class Habit(models.Model):
    name = models.CharField(max_length=32, default='')
    imgUrl = models.CharField(max_length=2048, default='')
    introduce = models.CharField(max_length=2048, default='')
    detailUrl = models.CharField(max_length=2048, default='')


class Illustrated(models.Model):
    did = models.IntegerField(default=0)
    introduce = models.CharField(max_length=2048, default='')
    method = models.CharField(max_length=2048, default='')
    diseasetype = models.CharField(max_length=2048, default='')


class Commodity(models.Model):
    gid = models.IntegerField(default=0)
    name = models.CharField(max_length=32, default='')
    price = models.FloatField(default=0)
    imgUrl = models.CharField(max_length=2048, default='')
    status = models.CharField(max_length=32, default='')
    remark = models.CharField(max_length=2048, default='')
    source = models.CharField(max_length=256, default='')


class Order(models.Model):
    buyers = models.CharField(max_length=32, default='')
    item = models.CharField(max_length=32, default='')
    number = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    consignee = models.CharField(max_length=32, default='')
    status = models.CharField(max_length=32, default='')
    address = models.CharField(max_length=128, default='')
    source = models.CharField(max_length=32, default='')


class Cart(models.Model):
    cid = models.IntegerField(default=0)
    user = models.CharField(max_length=32, default='')
    number = models.IntegerField(default=0)
    item = models.CharField(max_length=32, default='')
    price = models.FloatField(default=0)


class Message(models.Model):
    mid = models.IntegerField(default=0)
    name = models.CharField(max_length=32, default='')
    source = models.CharField(max_length=32, default='')
    subject = models.CharField(max_length=256, default='')
    info = models.CharField(max_length=2048, default='')
    email = models.CharField(max_length=256, default='')
    reply = models.CharField(max_length=2048, default='')
