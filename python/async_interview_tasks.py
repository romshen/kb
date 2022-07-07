import asyncio
import time

import aiohttp
import requests

DELAY1 = 1_000  # ms
DELAY2 = 2_000

URL1 = f"https://deelay.me/{DELAY1}/https://example.com/"
URL2 = f"https://deelay.me/{DELAY2}/https://example.com/"


def download_sync(url):
    with requests.Session() as sync_session:
        start_time = time.time()

        sync_session.get(url)

        finish_time = time.time() - start_time
        print(f"Downloaded synchronously from {url}" f"for: {round(finish_time, 1)}s")


async def download_async(url):
    async with aiohttp.ClientSession() as async_session:
        start_time = time.time()

        await async_session.get(url)

        finish_time = time.time() - start_time
        print(f"Downloaded asynchronously from {url}" f"for: {round(finish_time, 1)}s")


async def main():
    # option 1: create and await tasks
    #
    # task1 = asyncio.create_task(ssn.get(URL1))
    # task2 = asyncio.create_task(ssn.get(URL2))
    # await task1
    # await task2

    # option 2: await asyncio.gather
    #
    print("Running…")
    await asyncio.gather(
        asyncio.to_thread(download_sync, URL1),
        asyncio.to_thread(download_sync, URL2),
        download_async(URL1),
        download_async(URL2),
    )


if __name__ == "__main__":
    asyncio.run(main())

#
# output:
# Running…
# Downloaded asynchronously from https://deelay.me/1000/https://example.com/for: 2.4s
# Downloaded synchronously from https://deelay.me/1000/https://example.com/for: 2.6s
# Downloaded asynchronously from https://deelay.me/2000/https://example.com/for: 3.1s
# Downloaded synchronously from https://deelay.me/2000/https://example.com/for: 3.4s
