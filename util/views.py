from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.
def render_500(request):
    if request.is_ajax():
        err = {
            'error_code': 5,
            'error': 'Internal Server Error',
            'message': 'Internal Server Error',
        }
        return JsonResponse(err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return redirect('/error/?c=500')