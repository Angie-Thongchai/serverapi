from rest_framework.views import exception_handler


def custom_exception_handler(exc,context):

    handlers = {
        'validationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error
    }

    response = exception_handler(exc, context)

    if response is not None:
        if "AuthUserAPIView" in str(context[View]) and exc.status_code == 401:
            response.status_code = 200
            response.data = {'is_logged_in': False,
                             'status_code': 200}
        response.data['status_code'] = response.status_code

    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response

def _handle_authentication_error(exc, context, response):

    response.data = {
        'error': 'please login to proceed',
        'status_code': response.status_code
    }
    return response

def _handle_generic_error(exc, context, response):
    return response