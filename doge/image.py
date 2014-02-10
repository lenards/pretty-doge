"""
Magically manipulate and return the doge image.
"""
from math import floor

import numpy as np

from PIL import Image
from colorsys import rgb_to_hls, hls_to_rgb


LIGHT = (172, 143, 239)

DARK = (134, 30, 214)


def scrub_rgb(c):
    return (int(floor(c[0] * 255)),
            int(floor(c[1] * 255)),
            int(floor(c[2] * 255)))


def get_color_pallete(c):
    """
    Given a color c(rgb) return a new dark and light color(rgb).
    """
    hls_d = rgb_to_hls(c[0]/255., c[1]/255., c[2]/255.)
    # Magic numbers are the diff from hls(DARK) and hls(LIGHT).
    hls = (hls_d[0] - 0.04385, hls_d[1] + 0.27059, hls_d[2])
    new_dark = scrub_rgb(hls_to_rgb(hls_d[0], hls_d[1], hls_d[2]))
    new_light = scrub_rgb(hls_to_rgb(hls[0], hls[1], hls[2]))
    return new_light, new_dark


class ImageManager(object):
    """
    Manages the doge template and does the conversion.
    """
    _light = LIGHT
    _dark = DARK

    def __init__(self, image=None, light=None, dark=None):
        if light:
            self._light = light
        if dark:
            self._dark = dark
        if not image:
            self._image = Image.open("doge.png").convert("RGB")
        else:
            self._image = image.convert("RGB")
        self._data = np.array(self._image.convert("RGB"))

    def put_color(self, c):
        new_light, new_dark = get_color_pallete(c)
        return self.put(new_light, new_dark)

    def put(self, new_light, new_dark):
        data = np.copy(self._data)
        data[(data == LIGHT).all(axis=-1)] = new_light
        data[(data == DARK).all(axis=-1)] = new_dark
        return Image.fromarray(data, mode="RGB")
