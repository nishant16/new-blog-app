from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print ("welcome")

    def process_view(self,request,view_func,view_args,view_kwargs):
        #import pdb;pdb.set_trace()
        print (view_func.__name__)

    def process_response(self,request,response):
        print ("end")
        return response
