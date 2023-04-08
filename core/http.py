from django.http import HttpResponseRedirect


def redirect_back(request, redirect_url=None):
    url = request.META.get("HTTP_REFERER")

    if redirect_url:
        url = redirect_url

    return HttpResponseRedirect(url)
