import asyncio
import json

import time
from django.http import HttpResponse

DEFAULT_SLEEP_TIME = 1


def sync_sleep(request):
    sleep_time = float(request.GET.get('time', DEFAULT_SLEEP_TIME))
    time.sleep(sleep_time)
    return HttpResponse(json.dumps({'mode': 'sync', 'time': sleep_time}).encode())


async def async_sleep(request):
    sleep_time = float(request.GET.get('time', DEFAULT_SLEEP_TIME))
    await asyncio.sleep(sleep_time)
    return HttpResponse(json.dumps({'mode': 'async', 'time': sleep_time}).encode())
