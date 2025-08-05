from django.http import HttpResponse


def treatments(request):
    return HttpResponse("Hello, user! You're at the list of treatments.")