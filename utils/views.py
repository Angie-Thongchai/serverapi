from django.http import JsonResponse

def error_404(request, exception):
    message = ('The endpoint is not found')
    response = JsonResponse(data={'massage': message, 'status_code':404})
    response.status_code = 404
    return response

def error_500(request, Exception):
    message = ('An error occurred, its on us')
    response = JsonResponse(data={'massage': message, 'status_code':404})
    response.status_code = 500
    return response
