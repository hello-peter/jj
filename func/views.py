from django.shortcuts import render,HttpResponse
import os
import json
# Create your views here.
import sys
sys.path.append('../alpr_utils')
from alpr_utils import main as plate_compose
import mxnet as mx
from models import Police_account,User_account


def plate_recognize(request):
    	# 请求方法为PO5T时，进行处理
    if request.method == "POST":  
   	 	# 获取上传的文件，如果没有文件，则默认为None
        myFiles = request.FILES.getlist("myfile", None)  
        if not myFiles:
            return_res = {
                'plate' : 'no file'
            }
            return HttpResponse(json.dumps(return_res),content_type = "application/json;charset=UTF-8")
        for myFile in myFiles:
         	# 打开特定的文件进行二进制的写操作(有更新，无新建)
            fname = os.path.join("/home/kmust/Pictures", myFile.name)
            destination = open(fname, 'wb+') 
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
        
        
        context = mx.cpu()
        res = plate_compose.main(fname,context = context)
        return_res = {
            'plate' : res
        }
        print(res)
        return HttpResponse(json.dumps(return_res),content_type = 'application/json')

    if request.method == "GET":
        return render(request,'test.html')

#返回登陆状态
def police_login(request):
    if request.method == 'POST':
        usr_name = request.POST['name']
        password = request.POST['password']
        
        user_info = Police_account.objects.filter(name=usr_name).first()
        if usr_name == user_info.username and password == user_info.password:
            request.session.set_expiry(20000)
            request.session['islogin'] = 1
            request.session['name'] = usr_name
            log_info = {
                'success' : 1
            }
        else:
            lof_info = {
                'sucess' : 0
            }
            return HttpResponse(json.dumps(log_info),content_type = 'application/json')

def plice_logon(request):
    if request.method == "post":
        usr_name = request.POST['name']
        usr_name = request.POST['password']







