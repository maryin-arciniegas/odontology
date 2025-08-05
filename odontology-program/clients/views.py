from django.http import HttpResponse


def clients(request):
    return HttpResponse("Hello, client! You're at the list of clients.")

