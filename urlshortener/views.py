import uuid

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from urlshortener.models import Urlshortcut


def get_url(request):
    if request.method == 'GET':
        return render(request, 'shortener.html')
    elif request.method == 'POST':
        url = request.POST.get('url')
        if not url:
            return render(request, 'errormessage.html')
        shortcut = Urlshortcut()
        shortcut.address = url
        shortcut.shortcut = uuid.uuid4()  # generator of safe random values
        shortcut.save()
        base_url = request.get_host()
        output = base_url + '/' + str(shortcut.shortcut)
        context = {'outputURL': output}
        return render(request, 'output.html', context)
    else:
        return render(request, 'impropermethod.html')


def redirect_to_address(request, shortcut):
    to_address = Urlshortcut.objects.get(shortcut=shortcut)
    if not 'http' in to_address.address:
        to_address.address = 'http://' + to_address.address
    return HttpResponseRedirect(to_address.address, 302)
