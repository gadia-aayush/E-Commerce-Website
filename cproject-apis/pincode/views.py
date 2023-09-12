from django.shortcuts import render
from django.template.loader import get_template
import typesense
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseNotFound, Http404,  HttpResponseRedirect
from django.apps import apps
from django.db import models
from pincode.models import Pincodes
# Create your views here.
def cod_check(request, pin):
    q=Pincodes.objects.filter(pincode = pin).count()
    if q==0:
       return JsonResponse({'status':'unavailable'})
    else:
       return JsonResponse({'status':'available'})


def pin_check(request, pin):
    from pincode.models import PinMap
    q=PinMap.objects.filter(pincode = pin).values()
    result = list(q)
    return JsonResponse(result,safe=False)
