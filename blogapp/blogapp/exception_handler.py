from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def customer_exception_handler(exec, context):
    """ handles exceptions in a common way across the entire app """
    resp = exception_handler(exec, context)
    if resp is not None:
        return resp
    return Response({
        "detail": "Something went wrong, please try again later..."
    },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
