from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def generateTable(request):
    if request.method == 'POST':
        output = []
        num= int(request.POST['t1'])
        for i in range(1,11):
            rec=str(num)+'*'+str(i)+'='+str(i*num)
            output.append(rec)
        return render(request,'mtable.html', {'mtable': output})
    return render(request, 'mtable.html')
def calculator(request):
    if request.method == 'POST':
        val1= int(request.POST['t1'])
        val2= int(request.POST['t2'])
        if 'add' in request.POST:
            res=val1+val2
            action='Addition'
        #print(request.POST)
        elif 'sub' in request.POST:
            res=val2-val1
            action='Subtraction'
        elif'multi' in request.POST:
            res=val1*val2
            action='Multiplication'
        elif 'div' in request.POST:
            res=val1/val2
            action='Division'
        return render(request, 'calculator.html', {'result':res,'action':action})
        #return HttpResponse('claculator has recieved request')
    return render(request,'calculator.html')