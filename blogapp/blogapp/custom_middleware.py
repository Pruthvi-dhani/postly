import json
import logging
from io import BytesIO
from copy import deepcopy

from django.core.handlers.wsgi import WSGIRequest
from rest_framework.response import Response

from blogapp.logging_filters import clean_dict_keys


class RequestResponseLogging:
    """
    middleware that logs the request and response the django app receives
    """
    def __init__(self, get_response):
        # the callable view that this middleware receives
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        # log the request before moving on to the next view
        request_log_str = list()
        request_log_str.append("Request uri: " + request.get_full_path())
        request_log_str.append("Request method: " + request.method)
        request_log_str.append("Request headers: " + str(request.headers))
        # get the request body and reset it for further down the stack
        request_body = request.body
        try:
            parsed_request_body = json.loads(request_body)
            clean_dict_keys(parsed_request_body)
        except json.JSONDecodeError:
            # if json decoding fails then just decode the bytes to utf-8 str, and if any errors just replace them
            # with a 0 character
            parsed_request_body = request_body.decode(encoding="utf-8", errors="replace")
        # reset the request body for views/middleware down the line
        request._stream = BytesIO(request_body)
        request._read_started = False

        request_log_str.append("Request body: " + str(parsed_request_body))
        logging.info("\n".join(request_log_str))
        response: Response = self.get_response(request)
        # log the response before sending this back to the calling view
        response_log_str = list()
        response_log_str.append("Response headers: " + str(response.headers))
        response_data_copy = deepcopy(response.data)
        clean_dict_keys(response_data_copy)
        response_log_str.append("Response body: " + str(response_data_copy))
        logging.info("\n".join(response_log_str))
        return response
