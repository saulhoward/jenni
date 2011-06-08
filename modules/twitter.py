#!/usr/bin/env python

from httplib import HTTPConnection, HTTPSConnection
from urllib import quote
try:
    import json
except ImportError:
    import simplejson as json

def twitter(phenny, input):
    screen_name = input.group(2)

    conn = HTTPConnection('api.twitter.com')
    conn.request('GET', '/1/users/show.json?screen_name=%s' %
                        quote(screen_name))
    resp = conn.getresponse()
    conn.close()
    request = json.loads(resp.read())
    try:
      phenny.say('@%s: %s [%s]' % (screen_name, request['status']['text'],
                                 request['status']['created_at']))
    except KeyError:
      phenny.say("%s's timelime is not available." % screen_name)

twitter.commands = ['twitter']
twitter.example = '.twitter <name>'

if __name__ == '__main__':
    print __doc__.strip()
