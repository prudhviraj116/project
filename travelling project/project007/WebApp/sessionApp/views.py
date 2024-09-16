from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sessionexample(request):
    request.session.modified = True
    if request.method =='POST':
        data=request.POST['t1']
        if 'prev_data' in request.session:
            data=request.session['prev_data']+' '+data
            request.session['prev_data']=data
        else:
            request.session['prev_data']=data
        return render(request,'sessionapp/session.html',{'data':request.session['prev_data']})
    return render(request,'sessionapp/session.html')