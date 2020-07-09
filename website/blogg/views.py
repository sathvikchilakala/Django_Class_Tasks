from django.http import HttpResponse

def AboutUs(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Welcome to my AboutUs Page</h1></center><br></body>')
	
def Contact(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Welcome to my contact page</h1></center><br></body>')

def Product(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Welcome to my Product page</h1></center><br></body>')

def Hello(request):
	return HttpResponse('<body bgcolor="yellow"> <center><h1>Hello!!! Welcome to my blog page</h1></center><br></body>')

from django.http import HttpResponse
from django.shortcuts import render

def HelloTemplate(request):
	context={}
	return render(request,'hello.html',context)

def ProductStatic(request):
    context={}
    return render(request,'prod.html',context)

def ProductDynamicOneRecord(request):
    context={'pid':1001,'pname':'Django Framework','price':450,'author':'Milton'}
    return render(request,'prodonedy.html',context)

def Products(request):
    context={'proddb':[
    {'pid':101,'pname':'Dive into python 3','price':450,'author':'Milton'},
    {'pid':102,'pname':'Python algorithms','price':550,'author':'Charles'},
    {'pid':103,'pname':'Networking python','price':650,'author':'Miller'},
    {'pid':104,'pname':'Advanced python','price':350,'author':'Robert'},
    {'pid':105,'pname':'Python for automation','price':367,'author':'Smith'}
                      ]}
    return render(request,'prodsmultiple.html',context)

from .models import Post   
def BlogData(request): 
    context={'blogdb':Post.objects.all()}
    return render(request,'blog_data.html',context)

def bloggTest(request):
    context={}
    return render(request,'blogg/test.html',context)
