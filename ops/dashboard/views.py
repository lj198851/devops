from django.shortcuts import render, HttpResponse

# Create your views here.
def Index(request):
    print(request) #  打印对象
    print
    print(dir(request)) #  打印对象的属性
    return HttpResponse("Hello")
