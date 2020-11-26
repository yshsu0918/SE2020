from django.shortcuts import render
import requests
import json
# Create your views here.
from django.http import HttpResponse
import time

from .models import order_record
def getitems():
    url = 'http://140.113.167.23/se2020/product/all'
    r = requests.get(url)
    #print(r.text)
    Q = r.text[1:-1].replace('},{', '}@@@{')
    items = []
    for x in Q.split('@@@'):
        #print(x)
        json_object = json.loads(x)
        json_formatted_str = json.dumps(json_object, indent=2)
        print(json_formatted_str)
        items.append(json_object)    
    return items


def order_save(order):
    Q = order_record()
    Q.amount = order['amount']
    Q.item_id = order['item_id']
    Q.order_time = order['order_time']
    Q.valid = order['valid']
    Q.price = order['price']
    Q.total = order['total']
    print(Q)
    Q.save()

def sell(request):
    
    items = getitems()
    current_time = str(time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))
    return render(request, 'sell.html', locals() )


def ordering(request):
    items = getitems()
    print(items)
    reason = 'Just something wrong'
    if request.method == 'POST':
        print('get an order', request.POST)
        
        item_id = request.POST['item_id']
        print('item_id', item_id)

        amount = request.POST['id_'+item_id+'_amount']

        order = dict()
        order['amount'] = amount
        order['item_id'] = item_id
        order['order_time'] = str(time.strftime("%Y/%m/%d %H:%M:%S", time.gmtime()))        
        
        item = items[0]
        for itx in items:
            if itx['id'] == item_id:
                item = itx
                break
        
        order['price']= item['price']
        order['total'] = float(order['amount']) * int( order['price'] )

        if int(item['stock']) < int( amount ):
            reason = 'Sorry, we do not have enough item'
            order['valid'] = 'F'
            order_save(order)
            return render(request, 'error.html', locals() )
            
        else:
            order['valid'] = 'T'
            
            order_save(order)
            return render(request, 'ordering.html', locals() )

def Thank(request):
    return render(request, 'Thank.html', locals() )