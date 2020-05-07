from django.http import JsonResponse
from django.views import View
from rest_framework.parsers import JSONParser

from api.models import ProblemPrototype, ProblemHead
from api.serializers import ProblemPrototypeSerializer, ProblemHeadSerializer


# Create your views here.


class ProblemPrototypes(View):
    def get(self, request):
        prototypes = ProblemPrototype.objects.all()
        serializer = ProblemPrototypeSerializer(prototypes, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = JSONParser().parse(request)
        serializer = ProblemPrototypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def problem_heads(request, id=-1):
    if id != -1:
        heads = ProblemHead.objects.filter(prototype=id)
    else:
        heads = ProblemHead.objects.all()
    serializer = ProblemHeadSerializer(heads, many=True)
    return JsonResponse(serializer.data, safe=False)
