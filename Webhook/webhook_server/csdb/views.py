from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from . import models

# Create your views here.

CORS_HEADER_TAG = 'Access-Control-Allow-Origin'
CORS_HEADER = 'http://127.0.0.1:8080'

ANNOUNCE = 'announcements'
ANNOUNCE_TYPE = 'type'
ANNOUNCE_CONTENT = 'content'
FILE_ADDRESS = 'file_addr'


def testView(request, test):
    fileList = models.File.objects.all()
    response = JsonResponse({
        'test': test,
        'address': fileList[0].file_addr,
    }, headers={CORS_HEADER_TAG: CORS_HEADER})
    return response


def queryAnnouncement(request):
    announcements = models.Announcement.objects.all()
    announceEntries = []

    for announcement in announcements:
        entry = {
            ANNOUNCE_CONTENT: announcement.announce_text,
            ANNOUNCE_TYPE: announcement.announce_type,
            FILE_ADDRESS: announcement.file.file_addr,
        }
        announceEntries.append(entry)

    response = JsonResponse({
        ANNOUNCE: announceEntries,
    }, headers={CORS_HEADER_TAG: CORS_HEADER})
    return response
