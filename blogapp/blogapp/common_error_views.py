from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def custom_404_view(request, exception):
    """
    custom response body when django router can't find the route
    """
    return Response({
        "error": "Endpoint doesn't exist",
        "status_code": 404
    }, status=404)
