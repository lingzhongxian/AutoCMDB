from django.http.response import HttpResponse

def hello():
    return HttpResponse("Hello,World")

class User():
    def user(request):
        return HttpResponse("UserName is ling")