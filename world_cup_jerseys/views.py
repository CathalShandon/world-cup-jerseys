from django.shortcuts import render


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "404.html", status=404)


def error_500(request,):
    """"
    Handles HTTP 500 errors
    """
    return render(request, '500.html')
