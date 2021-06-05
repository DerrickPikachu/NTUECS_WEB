from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models

# Create your views here.


def testView(request, test):
    fileList = models.File.objects.all()
    response = JsonResponse({
        'test': test,
        'address': fileList[0].file_addr,
    })
    return response