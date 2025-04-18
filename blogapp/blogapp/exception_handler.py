import logging
import traceback

from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, ValidationError

from blogapp.custom_exceptions import CustomException


def customer_exception_handler(exec, context):
    """ handles exceptions in a common way across the entire app """
    resp = exception_handler(exec, context)
    if isinstance(exec, NotFound):
        return Response({
            "code": 404,
            "message": "the requested resource does not exist"
        }, status=status.HTTP_404_NOT_FOUND)
    if isinstance(exec, ValidationError):
        return Response({
            "code": exec.status_code,
            "message": exec.detail
        }, status=status.HTTP_400_BAD_REQUEST)
    if resp is not None:
        return resp
    if isinstance(exec, CustomException):
        return Response({
            "code": exec.code,
            "message": exec.message
        }, status.HTTP_200_OK)
    exception_trace = ''.join(traceback.TracebackException.from_exception(exec).format())
    logging.error("Received exception:" + str(exception_trace))
    return Response({
        "detail": "Something went wrong, please try again later..."
    },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
