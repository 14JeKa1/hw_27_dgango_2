import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.db import models




def root(request):
    return JsonResponse({"status": "ok"})

@method_decorator(csrf_exempt, name="dispatch")
class CategoryListCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        return JsonResponse({"id": cat.pk, "name": cat.name} for cat in categories)

    def post(self, request):
        data = json.loads(request.body)
        new_cat = Category.objects.create(name=data.get("name"))
        return JsonResponse()

