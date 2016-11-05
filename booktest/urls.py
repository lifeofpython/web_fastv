from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^detail/(?P<id>[0-9]*)/$',views.detail,name='detail'),
    # url(r'^goodlist/(?P<id>[0-9]*)/(?P<pIndex>[0-9]*)/(?P<psort>[0-9]*)/$',views.goodlist,name='goodlist')
    url(r'^list/(?P<listid>[0-9]*)/(?P<keywords>(price|time))/$',views.list,name="list"),
    url(r'^page/(?P<pIndex>[0-9]*)/$',views.pagelist,name='pagelist'),
    url(r'^addtocart/(?P<goodsid>[0-9]*)/$',views.addtocart,name="addtocart"),
  	url(r'^login/$',views.login,name="login")
    
    
]