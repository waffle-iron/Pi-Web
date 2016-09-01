from django.shortcuts import render, HttpResponse
from rest_framework.renderers import JSONRenderer
import json
from pprint import pprint
from .data import MATH_DATA


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def data(request):
    return JSONResponse(MATH_DATA)
