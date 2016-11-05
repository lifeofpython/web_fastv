#coding=utf-8
from django.shortcuts import *
from models import *
from django.core.paginator import Paginator
from web_util_tool import *
from django.http import *
from django.db.models import Q

@userinput
def index(request):

	return render(request,'booktest/index.html')
# @record_goods
def showtotals(request):
	if request.session.has_key("uname"):
		uname=request.session.get('uname')
		user=User_db.objects.get(user_name=uname)
		goodskind_info=user.cart_set.all()
		totalnums=0
		for goods in goodskind_info:
			totalnums+=goods.goods_num
		return totalnums
	else:
		totalnums=0
		return totalnums





def detail(request, id):
	gnews = Goods_info.objects.get(pk=id)
	glistnews=Goods_list.objects.get(pk=gnews.goods_list_id_id)
	glist=Goods_list.objects.all()
	grecommendlist = glistnews.goods_info_set.all()[1:3]
	dic = {
		'gnews':gnews,
		'glist':glist,
		'grecommendlist':grecommendlist,
		'glistnews':glistnews,
	}
	
	dic['totalnums']=showtotals(request)
	return render(request,"booktest/detail.html",dic)

def goodinfo(request,id,keywords):
	glistdetail = Goods_list.objects.get(pk=id)
	glist = Goods_list.objects.all()
	grecommendlist = glistdetail.goods_info_set.all().order_by("-id")[0:2]
	if keywords=="time":
		goods = Goods_info.objects.filter(goods_list_id_id=id)
	elif keywords=="price":
		goods = Goods_info.objects.filter(goods_list_id_id=id).order_by("goods_price")
	
	dic = {
		'glist':glist,
		'grecommendlist':grecommendlist,
		'glistdetail':glistdetail,
		'goods':goods,
		'keywords':keywords
	}
	
	dic['totalnums']=showtotals(request)

	return dic



def list(request,listid,keywords="time"):
	# readlist=request.session.get('recentRead')
 # 	print readlist
	request.session['listid']=listid
	request.session['keywords']=keywords
	dic = goodinfo(request,listid,keywords)
	goods=dic['goods']
	p = Paginator(goods,3)
	plist = p.page_range
	currentgoods=p.page(1)
	pMax=plist[-1]
	dic['plist']=plist
	dic['currentgoods']=currentgoods
	dic['pMax']=pMax
	dic['pIndex']=1
	return render(request,'booktest/list.html',dic)



def pagelist(request,pIndex):
	listid=request.session.get('listid')
	keywords=request.session.get('keywords')
	dic=goodinfo(request,listid,keywords)
	goods=dic['goods']
	pIndex=int(pIndex)
	p = Paginator(goods,3)
	plist = p.page_range
	currentgoods=p.page(pIndex)
	pMax=plist[-1]
	dic['plist']=plist
	dic['currentgoods']=currentgoods
	dic['pMax']=pMax
	dic['pIndex']=pIndex
	return render(request,'booktest/list.html',dic)

@login_required
def addtocart(request,id,*args):

	if Cart.objects.filter(goods_id_id=id):
		cart=Cart.objects.get(goods_id_id=id)
		cart.goods_num=cart.goods_num+int(request.POST["num"])
		cart.save()
	else:
		cart=Cart()
		cart.goods_id_id = id
		cart.goods_num = request.POST["num"]
		cart.user_id_id=1
		cart.save()
	return HttpResponseRedirect("/")

def login(request):
	return render(request,"booktest/login.html")

# def goodlist(request,id,pIndex="1",psort="1"):
# 	readlist=request.session.get('recentRead')
# 	print readlist
# 	glistdetail = Goods_list.objects.get(pk=id)
# 	glist = Goods_list.objects.all()
# 	grecommendlist = glistdetail.goods_info_set.all()[1:3]
# 	goods = Goods_info.objects.filter(goods_list_id_id=id)
# 	goodssort = Goods_info.objects.filter(goods_list_id_id=id).order_by("goods_price")
# 	psort = int(psort)
# 	if psort==1:
# 		p = Paginator(goods,3)
# 	else:
# 		p = Paginator(goodssort,3)
# 	plist = p.page_range
# 	pIndex=int(pIndex)
# 	currentgoods=p.page(pIndex)
# 	pMax=plist[-1]
# 	dic = {
# 		'glist':glist,
# 		'currentgoods':currentgoods,
# 		'grecommendlist':grecommendlist,
# 		'glistdetail':glistdetail,
# 		'plist':plist,
# 		'id':id,
# 		'pIndex':pIndex,
# 		'pMax':pMax,
# 		'goods':goods,
# 		'readlist':readlist
# 	}
# 	return render(request,"booktest/goodlist.html",dic)

@login_required
def addtocart(request,goodsid,dic):
	print goodsid
	userid=User_db.objects.get(user_name=dic["uname"]).id
	# print userid
	if Cart.objects.filter(user_id_id=userid):
		if Cart.objects.filter(user_id_id=userid).filter(goods_id_id=goodsid):
			cart=Cart.objects.filter(goods_id_id=goodsid).filter(user_id_id=userid)
			for cart in cart:
				cart.goods_num=cart.goods_num+int(request.POST.get("num",default=0))
				cart.save()
		else:
			cart=Cart()
			cart.goods_id_id = goodsid
			cart.goods_num = int(request.POST["num"])
			cart.user_id_id=User_db.objects.get(user_name=dic["uname"]).id
			cart.save()
	else:
		cart=Cart()
		cart.goods_id_id = goodsid
		cart.goods_num = int(request.POST["num"])
		cart.user_id_id=User_db.objects.get(user_name=dic["uname"]).id
		cart.save()

	return HttpResponseRedirect("/")

def login(request):
	return render(request,"booktest/login.html")

def userinput(request):

	request.session['uname']="lily"

	HttpResponse()



	
