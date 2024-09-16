def customMiddleware(get_response):
    def middleware(request):
        #before request reches views
        #print('inside custom middleware before view')
        #print(request.method)
        if request.method == 'GET':
         request.x = 'we are good students'
        else:
            request.x = 'we are not good students'
        resp=get_response(request)
        #before response reches client
        #print('inside custom middleware after view')
        return resp
    return middleware