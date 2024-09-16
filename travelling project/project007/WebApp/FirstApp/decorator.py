from django.shortcuts import redirect
def checkSuperUser(fun):
     
    def innerFun(request):
          if request.user.is_superuser==True:
               return fun(request)
          else:
               return redirect('homeurl')
    return innerFun

