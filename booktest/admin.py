from django.contrib import admin
from models import *
# Register your models here.
class Ord_inline(admin.StackedInline):
	model = Ord
	extra = 0

class Order_detali_inline(admin.StackedInline):
	model = Order_detail

class Goods_info_inline(admin.StackedInline):
	model = Goods_info

class Cart_inline(admin.StackedInline):
	model = Cart 

class Receiver_inline(admin.StackedInline):
	model = Receiver

@admin.register(User_db)
class User_db_admin(admin.ModelAdmin):
	list_display=['id','user_name','user_password','user_phone','user_email','user_address']
	list_per_page = 10
	inlines = [Ord_inline,Cart_inline,Receiver_inline]

@admin.register(Ord)
class Ord_admin(admin.ModelAdmin):
	list_display = ['id','order_user_id','order_num','submit_date','total_price','isPay']

@admin.register(Order_detail)
class Order_detail_admin(admin.ModelAdmin):
	list_display = ['id','odetail_goods_id','odetail_goods_num','odetail_totalprice','detail_num']
	list_per_page = 10

@admin.register(Goods_list)
class Goods_list_admin(admin.ModelAdmin):
	list_display = ['id','goods_list_name','goods_list_class','goods_list_pic']
	inlines = [Goods_info_inline]

@admin.register(Goods_info)
class Goods_info_admin(admin.ModelAdmin):
	list_display = ['id','goods_name','goods_description','goods_price','goods_stock','goods_msg','goods_unit','goods_pic_url','goods_detail_pic_url','goods_list_id']
	list_per_page = 10
	inlines = [Cart_inline]

@admin.register(Cart)
class Cart_admin(admin.ModelAdmin):
	list_display = ['id','goods_num','user_id','goods_id']
	list_per_page = 10

@admin.register(Receiver)
class Receiver_admin(admin.ModelAdmin):
	list_display = ['id','receiver_address','receiver_name','receiver_phone','receiver_user_id','receiver_email']
	list_per_page = 10

