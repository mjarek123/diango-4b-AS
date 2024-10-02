from django.http import HttpResponse
def index(request):
    return HttpResponse("Witaj na lekcji w ZSŁ!")