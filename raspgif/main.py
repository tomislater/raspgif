import click
import asyncio
import aiohttp

import constants


def fetch_content(url):
    respone = yield from aiohttp.request('GET', url)
    respone.close()


def get_images(parameter, when):
    urls = []
    for h in ["07", "08", "09"] + list(map(str, range(10, 20))):
        url = "{0}{1}.{2}.{3}00{4}".format(
            constants.RASP_URL,
            constants.parameters[parameter],
            constants.today if when == "today" else constants.tomorrow,
            h,
            constants.suffix,
        )
        urls.append(asyncio.Task(fetch_content(url)))
    yield from asyncio.gather(*urls)


@click.command()
@click.option('--parameter', help='The parameter.')
@click.option('--when', default="today", help='Today or tomorrow.')
def make_gif(parameter, when):
    loop = asyncio.get_event_loop()
    images = get_images(parameter, when)
    loop.run_until_complete(images)
    loop.close()


if __name__ == '__main__':
    make_gif()

