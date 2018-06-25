from .main import *

def not_found_handler(request):
    return render(request, '404.html')


def server_error_handler(request):
    return render(request, '500.html')

