from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.
def processing(request):
    #res=isinstance(request, HttpRequest)
    #print(res)
    #print(dir(HttpRequest))
    respobj = render(request,'second.html')
    return respobj
def greetings(request):
    if request.method =='POST':
       # print(request.POST)
        name=request.POST['t1']
        #return HttpResponse('Hello '+name)
        #return HttpResponse('Request received')
        return render(request,'result.html',{'name':name})
    return render(request,'greet.html')