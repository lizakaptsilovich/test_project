from django.http import HttpResponse

def check_host(request):
    return HttpResponse(f"HTTP_HOST: {request.get_host()}")