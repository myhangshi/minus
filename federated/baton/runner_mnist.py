import aiohttp
import asyncio
import async_timeout
 
async def fetch(session, url):
    with async_timeout.timeout(10000):
        async with session.get(url) as response:
            return await response.text()
 
async def main(loop):
     
    async with aiohttp.ClientSession(loop=loop) as session:
        for _ in range(1, 10): 
            print("\nissue get start_round request") 
            html = await fetch(session, 'http://127.0.0.1:6666/mnist/start_round')
            print(html)
            await asyncio.sleep(5)
            print("\nissue get client update request") 
            html = await fetch(session, 'http://127.0.0.1:6666/mnist/get_client_updates')
            print(html)
            await asyncio.sleep(3)
 
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))


