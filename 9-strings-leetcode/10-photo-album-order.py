from datetime import datetime

import sys

photos = """

photo.jpg, Warsaw, 2013-09-05 14:08:15

john.png, London, 2015-06-20 15:13:22

my-Friends.png, Warsaw, 2013-09-05 14:07:13

Eiffel.jpg, Paris, 2015-07-23 08:03:02

pisatower.jpg, Paris, 2015-07-22 23:59:59

BOB.jpg, London, 2015-08-05 00:02:03

notredame.png, Paris, 2015-09-01 12:00:00

me.jpg, Warsaw, 2013-09-06 15:40:22

a.png, Warsaw, 2016-02-13 13:33:50

b.jpg, Warsaw, 2016-01-02 15:12:22

c.jpg, Warsaw, 2016-01-02 14:34:30

d.jpg, Warsaw, 2016-01-02 15:15:01

e.png, Warsaw, 2016-01-02 09:49:09

f.png, Warsaw, 2016-01-02 10:5:32

g.jpg, Warsaw, 2016-02-29 22:13:11"""

def extract_timestamp(x_):

    return datetime.strptime(x_, '%Y-%m-%d %H:%M:%S')


def solutions(S):
    result = {}
    photo_arr = [k for k in S.split('\n') if k != '']
    for p in photo_arr:

        components = p.split(',')

        city = components[1].strip()

        if city not in result:

            result[city] = [p]

        else:

            result[city].append(p)

    zero_padding = {k:len(str(len(v)))-1 for k, v in result.items()}

    for dict_key, value in result.items():

        tmp = [(idx, row) for idx, row in

            enumerate(sorted(value, key=lambda x: extract_timestamp(x.split(',')[2].strip())))]

        result.update({dict_key: tmp})

    output = []

    for p in photo_arr:

        components = p.split(',')

        city = components[1].strip()

        ext = components[0].split('.')[1]

        ordering = [k[0] for k in result[city] if k[1] == p][0]+1

        padding = 0

        if zero_padding[city] > 0:

            if len(str(ordering)) - 1< zero_padding[city]:

                padding = zero_padding[city]

        res = city + '0' * padding + str(ordering) + '.' + ext

        output.append(res)

    return output


output = solutions(photos)
print(output)