from django.db.transaction import non_atomic_requests
from django.http import HttpResponse
from django.shortcuts import render
from pprint import pprint

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


# Create your views here.


@csrf_exempt
@require_POST
def amocrm_chats(request, scope_id):
    pprint(request.body)
    print(scope_id)
    return HttpResponse('test')