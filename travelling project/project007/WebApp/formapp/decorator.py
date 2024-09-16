from django.shortcuts import redirect
def checkSuperUser(fun):
     
    def innerFun(request):
          if request.user.is_superuser==True:
               return fun(request)
          else:
               return redirect('homeurl')
    return innerFun
def checkUser(allowed_groups=[]):
     def decFun(views_Fun):
          def innerFun(request):
               group_name=request.user.groups.all()[0].name
               if group_name in allowed_groups:
                    return views_Fun(request)
               else:
                    return redirect('homeurl')
          return innerFun
     return decFun