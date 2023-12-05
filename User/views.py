import re

from django.shortcuts import render

from User import models
from User.models import User, Administrator, Shops, Order, Cart, Commodity, Message, Recommend
from django.http.response import JsonResponse, HttpResponse
import pandas as pd


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = User.objects.filter(username=username)
        shops = Shops.objects.filter(username=username)
        admins = Administrator.objects.filter(username=username)
        print(user, shops, admins)
        if len(user) != 0:
            status = 'user'
            if user[0].password == password:
                return JsonResponse({"code": 200, "message": " ", "data": {"status": status}})
        elif len(shops) != 0:
            status = 'shops'
            if shops[0].password == password:
                return JsonResponse({"code": 200, "message": " ", "data": {"status": status}})
        elif len(admins) != 0:
            status = 'admin'
            if admins[0].password == password:
                return JsonResponse({"code": 200, "message": " ", "data": {"status": status}})


def getDatas(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = models.User.objects.get(username=username)
        user = {'username': user.username, 'identity': user.identity, 'telephone': user.telephone, 'area': user.area, 'species': user.species, 'province': user.province}
        recommend = models.Recommend.objects.all()
        recommend = pd.DataFrame.from_records(recommend.values(), columns=[field.name for field in recommend.model._meta.fields])
        recommend = {'name': recommend['name'].tolist(), 'imgUrl': recommend['imgUrl'].tolist(), 'detailUrl': recommend['detailUrl'].tolist()}
        recommend = [{'name': recommend['name'][i], 'imgUrl': recommend['imgUrl'][i], 'detailUrl': recommend['detailUrl'][i]} for i in range(len(recommend['name']))]

        habit = models.Habit.objects.all()
        habit = pd.DataFrame.from_records(habit.values(), columns=[field.name for field in habit.model._meta.fields])
        habit = {'name': habit['name'].tolist(), 'imgUrl': habit['imgUrl'].tolist(), 'introduce': habit['introduce'].tolist(), 'detailUrl': habit['detailUrl'].tolist()}
        habit = [{'name': habit['name'][i], 'imgUrl': habit['imgUrl'][i], 'introduce': habit['introduce'][i], 'detailUrl': habit['detailUrl'][i]} for i in range(len(habit['introduce']))]

        illustrated = models.Illustrated.objects.all()
        illustrated = pd.DataFrame.from_records(illustrated.values(), columns=[field.name for field in illustrated.model._meta.fields])
        illustrated = {'diseasetype': illustrated['diseasetype'].tolist(), 'introduce': illustrated['introduce'].tolist(), 'method': illustrated['method'].tolist()}
        illustrated = [{'diseasetype': illustrated['diseasetype'][i], 'introduce': illustrated['introduce'][i], 'method': illustrated['method'][i]} for i in range(len(illustrated['introduce']))]

        commodity = models.Commodity.objects.filter(status='在售')
        commodity = pd.DataFrame.from_records(commodity.values(), columns=[field.name for field in commodity.model._meta.fields])
        commodity = {'gid': commodity['gid'].tolist(), 'name': commodity['name'].tolist(), 'price': commodity['price'].tolist(), 'imgUrl': commodity['imgUrl'].tolist()}
        commodity = [{'gid': commodity['gid'][i], 'name': commodity['name'][i], 'price': commodity['price'][i], 'imgUrl': commodity['imgUrl'][i]} for i in range(len(commodity['name']))]

        order = models.Order.objects.filter(buyers=username)
        order = pd.DataFrame.from_records(order.values(), columns=[field.name for field in order.model._meta.fields])
        order = {'item': order['item'].tolist(), 'number': order['number'].tolist(), 'id': order['id'].tolist(),
                 'price': order['price'].tolist(), 'status': order['status'].tolist(),
                 'consignee': order['consignee'].tolist(), 'address': order['address'].tolist(), }
        order = [{'id': order['id'][i], 'item': order['item'][i], 'number': order['number'][i],
                  'price': order['price'][i], 'status': order['status'][i],
                  'consignee': order['consignee'][i], 'address': order['address'][i], } for i in range(len(order['address']))]

        cart = models.Cart.objects.filter(user=username)
        cart = pd.DataFrame.from_records(cart.values(), columns=[field.name for field in cart.model._meta.fields])
        cart = {'cid': cart['cid'].tolist(), 'number': cart['number'].tolist(), 'item': cart['item'].tolist(), 'price': cart['price'].tolist()}
        cart = [{'cid': cart['cid'][i], 'number': cart['number'][i], 'item': cart['item'][i], 'price': cart['price'][i]} for i in range(len(cart['price']))]

        message = models.Message.objects.filter(source=username)
        message = pd.DataFrame.from_records(message.values(), columns=[field.name for field in message.model._meta.fields])
        message = {'subject': message['subject'].tolist(), 'info': message['info'].tolist(), 'reply': message['reply'].tolist()}
        message = [{'subject': message['subject'][i], 'info': message['info'][i], 'reply': message['reply'][i]} for i in range(len(message['reply']))]
        return JsonResponse({"code": 200, "message": " ", 'data': {'recommend': recommend, 'habit': habit, 'illustrated': illustrated,
                                                                   'commodity': commodity, "order": order, 'cart': cart, "message": message, 'user': user}}, safe=False)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        identity = request.POST.get('identity')
        telephone = request.POST.get('telephone')
        if identity == '用户':
            User.objects.create(username=username, password=password, identity=identity, telephone=telephone)
            return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})
        elif identity == '商家':
            Shops.objects.create(username=username, password=password, identity=identity, telephone=telephone)
            return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def save(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        telephone = request.POST.get('telephone')
        province = request.POST.get('province')
        area = request.POST.get('area')
        species = request.POST.get('species')
        user = User.objects.get(username=username)
        user.telephone = telephone
        user.area = area
        user.province = province
        user.species = species
        user.save()
        return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def delete(request):
    if request.method == 'POST':
        typee = request.POST.get('type')
        idd = request.POST.get('id')
        if typee == '购物车':
            Cart.objects.filter(cid=idd).delete()
        else:
            Order.objects.filter(id=idd).delete()
        return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def admin(request):
    info = Recommend.objects.all()
    info = pd.DataFrame.from_records(info.values(), columns=[field.name for field in info.model._meta.fields])
    info = {'rid': info['rid'].tolist(), 'name': info['name'].tolist(), 'imgUrl': info['imgUrl'].tolist(), 'detailUrl': info['detailUrl'].tolist()}
    info = [{'rid': info['rid'][i], 'name': info['name'][i], 'imgUrl': info['imgUrl'][i], 'detailUrl': info['detailUrl'][i]} for i in range(len(info['detailUrl']))]

    account = User.objects.all()
    account = pd.DataFrame.from_records(account.values(), columns=[field.name for field in account.model._meta.fields])
    account = {'username': account['username'].tolist(), 'telephone': account['telephone'].tolist(), 'identity': account['identity'].tolist()}
    account = [{'username': account['username'][i], 'telephone': account['telephone'][i], 'identity': account['identity'][i]} for i in range(len(account['identity']))]

    merchant = Commodity.objects.filter(status='待审核')
    merchant = pd.DataFrame.from_records(merchant.values(), columns=[field.name for field in merchant.model._meta.fields])
    merchant = {'gid': merchant['gid'].tolist(), 'name': merchant['name'].tolist(), 'price': merchant['price'].tolist(), 'imgUrl': merchant['imgUrl'].tolist()}
    merchant = [{'gid': merchant['gid'][i], 'name': merchant['name'][i], 'price': merchant['price'][i], 'imgUrl': merchant['imgUrl'][i]} for i in range(len(merchant['name']))]

    message = Message.objects.filter(reply='')
    message = pd.DataFrame.from_records(message.values(), columns=[field.name for field in message.model._meta.fields])
    message = {'mid': message['mid'].tolist(), 'subject': message['subject'].tolist(), 'info': message['info'].tolist()}
    message = [{'mid': message['mid'][i], 'subject': message['subject'][i], 'info': message['info'][i]} for i in range(len(message['mid']))]

    return JsonResponse({"code": 200, "message": " ", 'data': {
        'info': info,
        'account': account,
        'merchant': merchant,
        'message': message
    }})


def personalInfo(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        province = user.province
        print(len(province))
        if len(province) != 0:
            print(6666)
            return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})
        else:
            username = request.POST.get('username')
            province = request.POST.get('province')
            area = request.POST.get('area')
            species = request.POST.get('species')
            print(username, province, area, species)
            user = User.objects.get(username=username)
            user.area = area
            user.province = province
            user.species = species
            user.save()
            if province:
                return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def getMerchants(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        sale = Commodity.objects.filter(source=username, status='在售')
        sale = pd.DataFrame.from_records(sale.values(), columns=[field.name for field in sale.model._meta.fields])
        sale = {'gid': sale['gid'].tolist(), 'name': sale['name'].tolist(), 'price': sale['price'].tolist(), 'status': sale['status'].tolist()}
        sale = [{'gid': sale['gid'][i], 'name': sale['name'][i], 'price': sale['price'][i], 'status': sale['status'][i]} for i in range(len(sale['name']))]

        forsale = Commodity.objects.filter(source=username, status='待审核')
        forsale = pd.DataFrame.from_records(forsale.values(), columns=[field.name for field in forsale.model._meta.fields])
        forsale = {'gid': forsale['gid'].tolist(), 'name': forsale['name'].tolist(), 'price': forsale['price'].tolist(), 'status': forsale['status'].tolist()}
        forsale = [{'gid': forsale['gid'][i], 'name': forsale['name'][i], 'price': forsale['price'][i], 'status': forsale['status'][i]} for i in range(len(forsale['name']))]

        stored = Commodity.objects.filter(source=username, status='仓库')
        stored = pd.DataFrame.from_records(stored.values(), columns=[field.name for field in stored.model._meta.fields])
        stored = {'gid': stored['gid'].tolist(), 'name': stored['name'].tolist(), 'price': stored['price'].tolist(), 'status': stored['status'].tolist()}
        stored = [{'gid': stored['gid'][i], 'name': stored['name'][i], 'price': stored['price'][i], 'status': stored['status'][i]} for i in range(len(stored['name']))]

        finished = models.Order.objects.filter(source=username, status='已完成')
        finished = pd.DataFrame.from_records(finished.values(), columns=[field.name for field in finished.model._meta.fields])
        finished = {'item': finished['item'].tolist(), 'number': finished['number'].tolist(), 'id': finished['id'].tolist(),
                    'price': finished['price'].tolist(), 'status': finished['status'].tolist(),
                    'consignee': finished['consignee'].tolist(), 'address': finished['address'].tolist(), }
        finished = [{'id': finished['id'][i], 'item': finished['item'][i], 'number': finished['number'][i],
                     'price': finished['price'][i], 'status': finished['status'][i],
                     'consignee': finished['consignee'][i], 'address': finished['address'][i], } for i in range(len(finished['address']))]

        toship = models.Order.objects.filter(source=username, status='待发货')
        toship = pd.DataFrame.from_records(toship.values(), columns=[field.name for field in toship.model._meta.fields])
        toship = {'item': toship['item'].tolist(), 'number': toship['number'].tolist(), 'id': toship['id'].tolist(),
                  'price': toship['price'].tolist(), 'status': toship['status'].tolist(),
                  'consignee': toship['consignee'].tolist(), 'address': toship['address'].tolist(), }
        toship = [{'id': toship['id'][i], 'item': toship['item'][i], 'number': toship['number'][i],
                   'price': toship['price'][i], 'status': toship['status'][i],
                   'consignee': toship['consignee'][i], 'address': toship['address'][i], } for i in range(len(toship['address']))]

        return JsonResponse({"code": 200, "message": " ", 'data': {'sale': sale, 'forsale': forsale, 'stored': stored, 'finished': finished, 'toship': toship}})


def getAccount(request):
    account = User.objects.all()
    account = pd.DataFrame.from_records(account.values(), columns=[field.name for field in account.model._meta.fields])
    account = {'username': account['username'].tolist(), 'telephone': account['telephone'].tolist(), 'identity': account['identity'].tolist()}
    account = [{'username': account['username'][i], 'telephone': account['telephone'][i], 'identity': account['identity'][i]} for i in range(len(account['username']))]
    return JsonResponse({"code": 200, "message": " ", 'data': {'account': account}})


def reply(request):
    if request.method == 'POST':
        mid = request.POST.get('mid')
        rep = request.POST.get('reply')
        print(mid, rep)
        message = Message.objects.get(mid=mid)
        message.reply = rep
        message.save()
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def audit(request):
    if request.method == 'POST':
        gid = request.POST.get('gid')
        status = request.POST.get('status')
        remark = request.POST.get('remark')
        print(gid, status)
        commodity = Commodity.objects.get(gid=gid)
        if status == 'yes':
            commodity.status = '在售'
        elif status == 'no':
            commodity.remark = remark
            commodity.status = '未通过'
        commodity.save()
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def accControl(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        oper = request.POST.get('oper')
        if oper == '删除':
            User.objects.filter(username=username).delete()
        elif oper == '重置':
            print('重置了，666')
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def infoControl(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        oper = request.POST.get('oper')
        if oper == '删除':
            User.objects.filter(username=username).delete()
        elif oper == '重置':
            print('重置了，666')
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def shopControl(request):
    if request.method == 'POST':
        idd = request.POST.get('id')
        oper = request.POST.get('oper')
        typee = request.POST.get('type')
        if typee == '商品':
            commodity = Commodity.objects.get(gid=idd)
            if oper == '下架':
                commodity.status = '仓库'
            elif oper == '撤销':
                commodity.status = '仓库'
            elif oper == '上架':
                commodity.status = '待审核'
            commodity.save()
        elif typee == '订单':
            if oper == '删除':
                Order.objects.filter(id=idd).delete()
            elif oper == '发货':
                order = Order.objects.get(id=idd)
                order.status = '已完成'
                order.save()
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def buyAndCart(request):
    if request.method == 'POST':
        typee = request.POST.get('type')
        idd = request.POST.get('id')
        username = request.POST.get('username')
        commodity = Commodity.objects.get(gid=idd)
        if typee == '购物车':
            Cart.objects.create(user=username, item=commodity.name, price=commodity.price, number=100, cid=5)
        else:
            Order.objects.create(buyers=username, item=commodity.name, price=commodity.price, number=100, id=5, source=commodity.source)
        return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def sendMessage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        info = request.POST.get('info')
        Message.objects.create(mid=2, name='白景阳', source=username, subject=subject, email=email, info=info, reply='')
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})


def settlement(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        cart = Cart.objects.filter(user=username)
        for one in cart:
            Order.objects.create(buyers=one.user, number=one.number, item=one.item, price=one.price, address='北京', consignee='lunar', source='shopper', status='待发货')
    return JsonResponse({"code": 200, "message": " ", 'data': {'status': 'ok'}})
