from django.shortcuts import render


def index(request):
    """Return the index-page of the application

    Args:
        request (HttpRequest): HTTP-request object from the browser

    Returns:
        HttpResponse: Renders and returns the 'index.html' template
    """

    return render(request, 'index.html')
