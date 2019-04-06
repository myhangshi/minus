import aiohttp
import asyncio
import async_timeout
 
async def fetch(session, url):
    with async_timeout.timeout(1000):
        async with session.get(url) as response:
            return await response.text()
 
async def main(loop):
    
    async with aiohttp.ClientSession(loop=loop) as session:
        html = await fetch(session, 'http://127.0.0.1:6666/linear/start_round')
        print(html)
        html = await fetch(session, 'http://127.0.0.1:6666/linear/get_client_updates')
        print(html)
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))


