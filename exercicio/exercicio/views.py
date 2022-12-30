import asyncio
from django.shortcuts import HttpResponse
import httpx


async def http_call_async():
    for num in range (1, 10):
        await asyncio.sleep(2)
        print(f'{num*2}s')
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")