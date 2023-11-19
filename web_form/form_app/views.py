from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from form_app.tiny_models import TinyModel


@api_view(['POST'])
def get_form_name(request):
    data = request.data
    if not data:
        return Response(request.data)
    form_name = TinyModel().get_form_name(data=data)
    if request.headers.get('User-Agent'):
        return Response(form_name)
    return JsonResponse(form_name)