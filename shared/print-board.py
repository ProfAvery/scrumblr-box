#!/usr/bin/env python

import datetime
import json
import operator
import os
import sys
import urlparse

import redis

MARGIN = 35
DEFAULT_SIZE = json.dumps({'width': 996, 'height': 466})

try:
    url = sys.argv[1]
except IndexError:
    bin = os.path.basename(sys.argv[0])
    print >>sys.stderr, 'Usage: %s url' % bin
    sys.exit(1)
(_, _, board, _, _, _) = urlparse.urlparse(url)

COLUMNS = '#scrumblr#-room:%s-columns' % board
SIZE = '#scrumblr#-room:%s-size' % board
CARDS = '#scrumblr#-room:%s-cards' % board

r = redis.Redis()
columns = r.lrange(COLUMNS, 0, -1)

size = json.loads(r.get(SIZE) or DEFAULT_SIZE)
width = float(size['width'])

ncolumns = len(columns)
column_width = width / ncolumns

cards = r.hgetall(CARDS)
card_list = []
for value in cards.itervalues():
    card = json.loads(value)
    column = int((card['x'] + MARGIN) / column_width)
    card['column'] = columns[column] if column < ncolumns else 'Other'
    card_list.append(card)

now = datetime.date.today()
header = 'Board as of %d-%02d-%02d' % (now.year, now.month, now.day)
print header
print '=' * len(header)
print

for column in columns + ['Other']:
    this_column = [card for card in card_list if card['column'] == column]
    this_column.sort(key=operator.itemgetter(u'y'))
    print column
    print '-' * len(column)
    for card in this_column:
        if card['sticker'] and card['sticker'] != 'nosticker':
            print ' - **' +  card['text'] + '**'
        else:
            print ' - ' + card['text']
    print

