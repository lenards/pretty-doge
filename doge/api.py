import StringIO
from string import hexdigits

from flask import Flask, abort, make_response, send_file, request

from PIL.ImageColor import getrgb

from werkzeug.contrib.cache import MemcachedCache

import image as doge_image


cache = MemcachedCache(['127.0.0.1:11211'])

im = doge_image.ImageManager()

app = Flask(__name__)

def hash_to_color(digest):
    """
    Given a 32 or 40 character hexidecimal string, return a
    color as an integer three-tuple.
    """
    color = int(digest, 16) % (2 ** 24)
    return tuple([color / 2 ** (8 * i) % 2 ** 8 for i in xrange(3)])

def get_color(color):
    """
    Interpret some string as a color represented as a integer three tuple
    """
    if (len(color) == 32 or len(color) == 40)\
       and all(c in hexdigits for c in color):
        return hash_to_color(color)
    try:
        return getrgb(color)
    except:
        return getrgb("#" + color)


@app.route("/<color>")
def doge_color(color):
    if cache.get(color):
        return send_file(cache.get(color), mimetype="image/png")
    try:
        io = StringIO.StringIO()
        print "color = %s" % color
        image = im.put_color(get_color(color))
        image.save(io, "PNG")
        io.seek(0)
        cache.set(color, io, timeout=60*60)
        return send_file(io, mimetype="image/png")
    except Exception as e:
        print e
        return abort(404)


@app.route("/")
def doge():
    color = request.args.get("color", "#343434")
    return doge_color(color)


if __name__ == "__main__":
    app.run()
