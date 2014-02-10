"""
Utility methods for pretty-doge.

NOTE: These methods were used in development but are not currently used.
"""


WHITE = (255, 255, 255)

BLACK = (0, 0, 0)


def choose(color):
    """
    Used to convert the png into 4 color.
    """
    r, g, b, a = color
    if r < 90:
        return (0, 0, 0, 255)
    if r >= 77 and r < 160:
        return (134, 30, 214, 255)
    if r >= 160 and r < 208:
        return (172, 143, 239, 255)
    else:
        return (255, 255, 255, 255)


def put_orig(self, n):
    im = self._image.copy()
    new_light, new_dark = get_pallete(n, LIGHT, DARK)
    c = 0
    for i in range(0, 240):
        for j in range(0, 240):
            p = im.getpixel((i, j))
            if p == LIGHT:
                c += 1
                im.putpixel((i, j), new_light)
            else:
                if p == DARK:
                    c += 1
                    im.putpixel((i, j), new_dark)
    return im


def put_n(self, n):
    new_light, new_dark = get_pallete(n, LIGHT, DARK)
    return self.put(new_light, new_dark)


def get_h(h, n):
    if n < 50:
        return h - h * (n / 100.)
    else:
        return h + h * (n / 100.)


def get_pallete(n, l, d):
    hls = rgb_to_hls(l[0]/255., l[1]/255., l[2]/255.)
    hls_d = rgb_to_hls(d[0]/255., d[1]/255., d[2]/255.)
    h_mod = get_h(hls[0], n)
    h_mod_d = get_h(hls_d[0], n)
    new_light = scrub_rgb(hls_to_rgb(h_mod, hls[1], hls[2]))
    new_dark = scrub_rgb(hls_to_rgb(h_mod_d, hls_d[1], hls_d[2]))
    return new_light, new_dark
