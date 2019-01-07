from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Myinfo, Trade_info, SR_info
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
import requests, json

# Create your views here.
URL = 'http://54.180.31.9:8545'

def create_account(request):
    data = request
    response = requests.post(URL, json=data)
    response = response.json()
    return response

def balance_money_chain(request):
    data = request
    response = requests.post(URL, json=data)
    response = response.json()
    return response

@login_required
def cancel_info(request):
    if request.method == "GET":
        inx = request.GET.get('inx')
        SR_info.objects.filter(inx=inx).update(status_reg=False)
        return render(request, 'cancel_info_complete.html', {})

@login_required
def trade_view(request):
    if request.method == "GET":
        inx = request.GET.get('inx')
        db = SR_info.objects.get(inx=inx)
        myusername = request.user.get_username()
        if db.send_id == myusername:
            username = db.receive_id
            tmp = '1'
        else:
            username = db.send_id
            tmp = '2'
        return render(request, 'trade_view.html', {'db': db, 'username': username, 'tmp': tmp})
    else:
        return render(request, 'trade_view.html', {})

@login_required
def send_money(request):
    if request.method == "POST":
        try:
            data = Myinfo.objects.get(id=request.POST['receive_id'])
        except EmptyPage:
            return render(request, 'send_money_false.html', {})

        username = request.user.get_username()
        data2 = Myinfo.objects.get(id=username)
        block_query = {"jsonrpc": "2.0", "id": 10, "method": "personal_unlockAccount", "params": [data2.myaccount_reg, data2.myaccount_password, 300]}
        response = balance_money_chain(block_query)
        money = hex(int(request.POST['send_money'])*1000000000000000000)
        block_query = {"jsonrpc": "2.0", "id": 10, "method": "eth_sendTransaction", "params": [{"from":data2.myaccount_reg, "to":data.myaccount_reg, "value":money}]}
        response = balance_money_chain(block_query)

        db = SR_info()
        db.send_id = request.POST['send_id']
        db.receive_id = request.POST['receive_id']
        db.send_money = request.POST['send_money']
        db.date_reg = timezone.now()
        db.status_reg = True
        db.gubun_reg = 'money'
        db.value_reg = response["result"]
        db.save()

        #receive_user = Myinfo.objects.get(id=request.POST['receive_id'])
        #receive_amount = int(receive_user.amount_reg) + int(request.POST['send_money'])
        #Myinfo.objects.filter(id=request.POST['receive_id']).update(amount_reg=receive_amount)
        #send_user = Myinfo.objects.get(id=request.POST['send_id'])
        #send_amount = int(send_user.amount_reg) - int(request.POST['send_money'])
        #Myinfo.objects.filter(id=request.POST['send_id']).update(amount_reg=send_amount)

    username = request.user.get_username()
    if Myinfo.objects.filter(id=username).count() == 0:
        return render(request, 'send_money_false.html', {})
    else:
        db = Myinfo.objects.get(id=username)
        amount = db.amount_reg
        data = {"jsonrpc": "2.0", "id": 1, "method": "eth_getBalance", "params": [db.myaccount_reg, "latest"]}
        response = balance_money_chain(data)
        response = int(response["result"], 16)
        response = response / 1000000000000000000
        return render(request, 'send_money.html', {'amount': response})

@login_required
def send_info(request):
    if request.method == "POST":
        data = Myinfo.objects.filter(id=request.POST['receive_id'])
        try:
            username_box = request.POST['username_box']
        except EmptyPage:
            username_box = False
        try:
            name_reg_box = request.POST['name_reg_box']
        except:
            name_reg_box = False
        try:
            email_reg_box = request.POST['email_reg_box']
        except:
            email_reg_box = False
        try:
            jumin_number_box = request.POST['jumin_number_box']
        except:
            jumin_number_box = False
        try:
            phone_number_box = request.POST['phone_number_box']
        except:
            phone_number_box = False
        try:
            sex_reg_box = request.POST['sex_reg_box']
        except:
            sex_reg_box = False
        try:
            marry_reg_box = request.POST['marry_reg_box']
        except:
            marry_reg_box = False

        if len(data) != 0:
            username = request.user.get_username()
            data2 = Myinfo.objects.get(id=username)
            block_query = {"jsonrpc": "2.0", "id": 10, "method": "personal_unlockAccount",
                           "params": [data2.myaccount_reg, data2.myaccount_password, 300]}
            response = balance_money_chain(block_query)
            value_reg = '1'
            money = hex(int('1000000000000000000'))
            data = Myinfo.objects.get(id=request.POST['receive_id'])
            block_query = {"jsonrpc": "2.0", "id": 10, "method": "eth_sendTransaction",
                           "params": [{"from": data2.myaccount_reg, "to": data.myaccount_reg, "value": money}]}
            response = balance_money_chain(block_query)
            db = SR_info()
            #phone_number_box = request.POST['phone_number_box']
            if username_box != False:
                db.send_id = request.POST['username']
            if name_reg_box != False:
                db.name_reg = request.POST['name_reg']
            if email_reg_box != False:
                db.email_reg = request.POST['email_reg']
            if jumin_number_box != False:
                db.jumin_number = request.POST['jumin_number']
            if phone_number_box != False:
                db.phone_number = request.POST['phone_number']
            if sex_reg_box != False:
                db.sex_reg = request.POST['sex_reg']
            if marry_reg_box != False:
                db.marry_reg = request.POST['marry_reg']
            db.receive_id = request.POST['receive_id']
            db.date_reg = timezone.now()
            db.status_reg = True
            db.gubun_reg = 'info'
            db.value_reg = response["result"]
            db.save()
        else:
            return render(request, 'send_info_false.html', {})

    username = request.user.get_username()
    if Myinfo.objects.filter(id=username).count() == 0:
        marry_reg = ""
        marry_reg_len = len(marry_reg)
        sex_reg = ""
        sex_reg_len = len(sex_reg)
        return render(request, 'send_info.html', {'marry_reg': marry_reg, 'marry_reg_len': marry_reg_len, 'sex_reg': sex_reg,
                                             'sex_reg_len': sex_reg_len})

    data = Myinfo.objects.get(id=username)
    name_reg = data.name_reg
    email_reg = data.email_reg
    jumin_number = data.jumin_number
    phone_number = data.phone_number
    sex_reg = data.sex_reg
    marry_reg = data.marry_reg
    marry_reg_len = len(marry_reg)
    sex_reg_len = len(sex_reg)
    return render(request, 'send_info.html', {'marry_reg': marry_reg, 'marry_reg_len': marry_reg_len, 'sex_reg': sex_reg,
                                         'sex_reg_len': sex_reg_len,
                                         'name_reg': name_reg, 'email_reg': email_reg, 'jumin_number': jumin_number,
                                         'phone_number': phone_number})

@login_required
def send_trade_list(request):
    username = request.user.get_username()
    #data = SR_info.objects.filter(send_id=username)|SR_info.objects.filter(receive_id=username)
    page_data = Paginator(SR_info.objects.filter(send_id=username).order_by('inx')[:150], 15)
    page = request.GET.get('page')
    try:
        data = page_data.page(page)
    except PageNotAnInteger:
        data = page_data.page(1)
    except EmptyPage:
        data = page_data.page(page_data.num_pages)
    return render(request, 'send_trade_list.html', {'data': data, 'current_page': page, 'total_page': range(1, page_data.num_pages + 1)})

@login_required
def receive_trade_list(request):
    username = request.user.get_username()
    #data = SR_info.objects.filter(send_id=username)|SR_info.objects.filter(receive_id=username)
    page_data = Paginator(SR_info.objects.filter(receive_id=username).order_by('inx')[:150], 15)
    page = request.GET.get('page')
    try:
        data = page_data.page(page)
    except PageNotAnInteger:
        data = page_data.page(1)
    except EmptyPage:
        data = page_data.page(page_data.num_pages)
    return render(request, 'receive_trade_list.html', {'data': data, 'current_page': page, 'total_page': range(1, page_data.num_pages + 1)})

@login_required
def charge_money(request):
    if request.method == "POST":
        username = request.POST['username']
        charge_money = request.POST['charge_money']
        charge_money = int(charge_money)
        db = Myinfo.objects.get(id=username)
        charge_money = db.amount_reg + charge_money
        Myinfo.objects.filter(id=username).update(amount_reg=charge_money)
        return HttpResponseRedirect(reverse("amount"))

    username = request.user.get_username()
    if Myinfo.objects.filter(id=username).count() == 0:
        return render(request, 'charge_money_false.html', {'marry_reg': 'marry_reg'})
    else:
        db = Myinfo.objects.get(id=username)
        amount = db.amount_reg
        dataa = {"jsonrpc": "2.0", "id": 1, "method": "eth_getBalance", "params": [db.myaccount_reg, "latest"]}
        response = balance_money_chain(dataa)
        response = int(response["result"], 16)
        response = response / 1000000000000000000
        #amount = Myinfo.objects.filter(id=userna
        return render(request, 'charge_money.html', {'amount': response})

@login_required
def amount(request):
    username = request.user.get_username()
    if Myinfo.objects.filter(id=username).count() != 0:
        data = Myinfo.objects.get(id=username)
        amount = data.amount_reg
        dataa = {"jsonrpc": "2.0", "id": 1, "method": "eth_getBalance", "params": [data.myaccount_reg, "latest"]}
        response = balance_money_chain(dataa)
        response = int(response["result"], 16)
        response = response / 1000000000000000000
        #amount = Myinfo.objects.filter(id=username).count()
        Myinfo.objects.filter(id=username).update(amount_reg=response)
        return render(request, 'amount.html', {'amount': response})
    else:
        amount = '0'
        return render(request, 'amount.html', {'amount': amount})

@login_required
def edit(request):
    if request.method == "POST":
        username = request.POST['username']
        name_reg = request.POST['name_reg']
        email_reg = request.POST['email_reg']
        jumin_number = request.POST['jumin_number']
        phone_number = request.POST['phone_number']
        sex_reg = request.POST['sex_reg']
        marry_reg = request.POST['marry_reg']
        myaccount_reg = request.POST['myaccount_reg']
        if Myinfo.objects.filter(id=username).count() == 0:
            db = Myinfo()
            db.id = username
            db.name_reg = name_reg
            db.email_reg = email_reg
            db.jumin_number = jumin_number
            db.phone_number = phone_number
            db.sex_reg = sex_reg
            db.marry_reg = marry_reg
            db.myaccount_password = myaccount_reg
            data = {"jsonrpc": "2.0", "id": 10, "method": "personal_newAccount", "params": [myaccount_reg]}
            hash_account = create_account(data)
            db.myaccount_reg = hash_account["result"]
            db.save()
            return HttpResponseRedirect(reverse("view"))
        else:
            Myinfo.objects.filter(id=username).update(name_reg=name_reg, email_reg=email_reg, jumin_number=jumin_number,
                                                        phone_number=phone_number, sex_reg=sex_reg, marry_reg=marry_reg)
            return HttpResponseRedirect(reverse("view"))

    username = request.user.get_username()
    if Myinfo.objects.filter(id=username).count() == 0:
        marry_reg = ""
        marry_reg_len = len(marry_reg)
        sex_reg = ""
        sex_reg_len = len(sex_reg)
        myaccount_reg = "0"
        return render(request, 'edit.html', {'marry_reg':marry_reg, 'marry_reg_len':marry_reg_len, 'sex_reg':sex_reg,
                                             'sex_reg_len':sex_reg_len, 'myaccount_reg': myaccount_reg})
    else:
        data = Myinfo.objects.get(id=username)
        name_reg = data.name_reg
        email_reg = data.email_reg
        jumin_number = data.jumin_number
        phone_number = data.phone_number
        sex_reg = data.sex_reg
        marry_reg = data.marry_reg
        marry_reg_len = len(marry_reg)
        sex_reg_len = len(sex_reg)
        myaccount_reg = data.myaccount_reg
        return render(request, 'edit.html', {'marry_reg':marry_reg, 'marry_reg_len':marry_reg_len, 'sex_reg':sex_reg, 'sex_reg_len':sex_reg_len,
                                             'name_reg':name_reg, 'email_reg':email_reg, 'jumin_number':jumin_number,
                                             'phone_number':phone_number, 'myaccount_reg': myaccount_reg})

@login_required
def view(request):
    username = request.user.get_username()
    if Myinfo.objects.filter(id=username).count() == 0:
        marry_reg = ""
        marry_reg_len = len(marry_reg)
        sex_reg = ""
        sex_reg_len = len(sex_reg)
        myaccount_reg = "0"
        return render(request, 'edit.html', {'marry_reg': marry_reg, 'marry_reg_len': marry_reg_len, 'sex_reg': sex_reg,
                                             'sex_reg_len': sex_reg_len, 'myaccount_reg': myaccount_reg})

    data = Myinfo.objects.get(id=username)
    name_reg = data.name_reg
    email_reg = data.email_reg
    jumin_number = data.jumin_number
    phone_number = data.phone_number
    sex_reg = data.sex_reg
    marry_reg = data.marry_reg
    marry_reg_len = len(marry_reg)
    sex_reg_len = len(sex_reg)
    myaccount_reg = data.myaccount_reg
    return render(request, 'view.html', {'marry_reg': marry_reg, 'marry_reg_len': marry_reg_len, 'sex_reg': sex_reg,
                                         'sex_reg_len': sex_reg_len,
                                         'name_reg': name_reg, 'email_reg': email_reg, 'jumin_number': jumin_number,
                                         'phone_number': phone_number, 'myaccount_reg': myaccount_reg})
