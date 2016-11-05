from django.http import HttpResponseRedirect, HttpResponse



def login_required(func):
    def wrapper(request,goodsid,*args, **kw):
        user = request.session.get('uname', default='')
        dic={}
        if user:
            dic = {
                'uname': user           
            }
           
            return func(request,goodsid,dic, *args, **kw)
        return HttpResponseRedirect('/login/')
    return wrapper


def record_goods(func):
    def wrapper(request, id, *args, **kw):
        sessionList = request.session.get('recentRead')
        if sessionList:
            sessionLength = len(sessionList)
            
            if sessionLength > 4:
                sessionList.pop()
                sessionList.insert(0,id)
                request.session['recentRead'] = sessionList

            elif sessionLength < 4 and sessionLength > 0:
                sessionList.append(id)
                request.session['recentRead'] = sessionList
        else:
            readList = []
            readList.append(id)
            request.session['recentRead'] = readList

        return func(request, id, *args, **kw)
    return wrapper


def rand_num(userName, user_phone):
    from random import randint
    import hashlib
    from time import localtime

    time = localtime()

    numTotal = str(time.tm_year) + str(time.tm_mon) + str(time.tm_mday) + str(time.tm_sec)\
                + str(time.tm_min) + str(time.tm_hour) + userName + user_phone
    md5 = hashlib.md5()
    md5.update(numTotal)
    order_num =  md5.hexdigest()
    return (order_num, time)


def userinput(func):
    def wrapper(request):
        request.session['uname']="yazhouhan"
        return func(request)
    return wrapper














