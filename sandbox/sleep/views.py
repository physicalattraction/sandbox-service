import asyncio
import json
import time

from django.http import HttpResponse

from sleep.utils import measure_time, parse_float

DEFAULT_SLEEP_TIME = 1


async def async_sleep(request):
    sleep_time = parse_float(request.GET.get('time', DEFAULT_SLEEP_TIME))
    with measure_time() as t:
        await asyncio.sleep(sleep_time)
    return HttpResponse(json.dumps({'mode': 'async', 'time': sleep_time, 'elapsed_time': str(t)}).encode())


def sync_sleep(request):
    sleep_time = parse_float(request.GET.get('time', DEFAULT_SLEEP_TIME))
    with measure_time() as t:
        time.sleep(sleep_time)
    return HttpResponse(json.dumps({'mode': 'sync', 'time': sleep_time, 'elapsed_time': str(t)}).encode())
