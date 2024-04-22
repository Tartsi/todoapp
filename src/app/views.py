from django.shortcuts import render


def index(request):
    """Return the index-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'index.html' template
    """

    return render(request, 'index.html')


def register(request):
    """Returns the registration-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'register.html' template
    """

    return render(request, 'register.html')
