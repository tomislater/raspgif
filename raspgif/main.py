import sys
import click
import asyncio
import aiohttp

import constants
from subprocess import call


@asyncio.coroutine
def fetch_content(url):
    response = yield from aiohttp.request('GET', url)
    return (yield from response.read())


def get_images(parameter, when):
    urls = []
    for h in constants.hours:
        url = "{0}{1}.{2}.{3}00{4}".format(
            constants.RASP_URL,
            constants.parameters[parameter],
            constants.today if when == "today" else constants.tomorrow,
            h,
            constants.suffix,
        )
        urls.append(asyncio.get_event_loop().run_until_complete(fetch_content(url)))
    return urls


@click.command()
@click.option('--parameter', help='The parameter.')
@click.option('--when', default="today", help='Today or tomorrow.')
def make_gif(parameter, when):
    images = get_images(parameter, when)
    for img, h in zip(images, constants.hours):
        with open('raspgif/pngs/{0}.png'.format(h), 'wb') as f:
            f.write(img)

    call(["convert", "-delay", "80", "-loop", "0", "raspgif/pngs/*png", "animated.gif"])
    with open("animated.gif", "rb") as f:
        sys.stdout.buffer.write(f.read())


if __name__ == '__main__':
    make_gif()

