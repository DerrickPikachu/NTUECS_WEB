from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models

# Create your views here.

CORS_HEADER_TAG = 'Access-Control-Allow-Origin'
CORS_HEADER = 'http://127.0.0.1:8080'


def testView(request, test):
    fileList = models.File.objects.all()
    response = JsonResponse({
        'test': test,
        'address': fileList[0].file_addr,
    }, headers={CORS_HEADER_TAG: CORS_HEADER})
    return response
