#
#  Check the trains schedule (Renfe, Spain)
#  ===================================================
#
#    Provides a class to check the timetable of the
#    trains in Spain.
#
#    Jose Ignacio Galarza
#    <igalarzab@gmail.com>
#

import argparse
from datetime import datetime, timedelta, time
import re
import sys

from lxml import etree
import requests

# Global information
__uname__ = 'pyrenfe'
__long_name__ = 'Train checker (Cercanias Renfe, Spain)'
__version__ = '2.0'
__author__ = 'Jose Ignacio Galarza'
__email__ = 'igalarzab@gmail.com'
__url__ = 'http://github.com/igalarzab/pyrenfe'
__license__ = 'MIT'

class RenfeRoute(object):
    'A renfe route between two stations'

    # API URL (XML)
    URL = 'http://horarios.renfe.com/cer/horarios/horarios.jsp'

    def __init__(self, rfrom, rto):
        'Initialize the route between an origin an a destine'
        self.rfrom = rfrom
        self.rto = rto

    def timetable(self, day=None, initialHour=0, finalHour=24):
        'Show the timetable of the renfe route'
        if not day:
            day = datetime.now().strftime('%Y%m%d')

        if not re.match(r'^\d{8}$', day):
            raise ValueError('Incorrect date format, must be %Y%m%d')

        if initialHour < 0 or initialHour > 24 or \
           finalHour < 0 or finalHour > 24:
            raise ValueError('Time values must be between 0 and 23')

        return self._downloadTimetable(day, initialHour, finalHour)

    def nextTrain(self, quantity=1, margin=5):
        'Show the next *quantity* trains, with *margin* minutes'
        now = datetime.now()

        today = now.strftime('%Y%m%d')
        hour = now.strftime('%H')

        # Calculates the limit range to search
        limitMinute = (now.minute + margin) % 60
        limitHour = now.hour if (now.minute + margin) < 60 else (now.hour + 1)
        nowLimit = time(limitHour, limitMinute)

        timetable = self._downloadTimetable(today, hour)

        for i in range(len(timetable)):
            if timetable[i]['leave'] > nowLimit:
                return timetable[i:i + quantity]

        return None

    def _downloadTimetable(self, day, initialHour=0, finalHour=24):
        'Download the timetable from renfe.com'
        params = {
            'nucleo': '10',
            'o': self.rfrom,
            'd': self.rto,
            'df': day,
            'ho': initialHour,
            'hd': finalHour
        }

        req = requests.get(RenfeRoute.URL, params=params)
        timetable = etree.fromstring(req.content)
        trains_timetable = []

        if timetable[0].text.strip() == 'Datos no disponibles.':
            raise ValueError('Invalid origin or destine')

        for t in timetable[3]:
            duration = [int(x) for x in t[3].text.split(':')]

            trains_timetable.append({
                'train': t[0].text.strip(),
                'leave': time(*[int(x) for x in t[1].text.split(':')]),
                'arrive': time(*[int(x) for x in t[2].text.split(':')]),
                'time': timedelta(*duration),
            })

        return trains_timetable


class TimetablePrinter(object):
    'Pretty print timetables'

    @staticmethod
    def as_table(timetable):
        'Print the timetable as a table'
        print('-' * 41)
        print('|   Leaves   |   Arrives  |     Line    |')
        print('-' * 41)

        for tt in timetable:
            print('|%(leave)10s  |%(arrive)10s  |%(train)08s     |' % tt)
            print('-' * 41)

    @staticmethod
    def as_text(timetable):
        'Print the timetable as human text'
        for tt in timetable:
            print('Next train leaves at %(leave)s and '
                  'arrives at %(arrive)s (line %(train)s)' % tt)

    @staticmethod
    def as_notification(timetable):
        'Raise a notification with pynotify'
        pass  # TODO: Use pynotify


def create_parser():
    'Parse the program arguments'
    pparser = argparse.ArgumentParser(description='Check Renfe schedule')

    pparser.add_argument('--version',
                         action='version',
                         version='%s %s' % (__uname__, __version__))

    pparser.add_argument('-o', '--origin',
                         dest='origin',
                         required=True,
                         metavar='RENFE_ID',
                         type=int,
                         help='origin renfe station (id, a number)')

    pparser.add_argument('-d', '--destine',
                         dest='destine',
                         required=True,
                         metavar='RENFE_ID',
                         type=int,
                         help='destine renfe station (id, a number)')

    action = pparser.add_mutually_exclusive_group()

    action.add_argument('-t', '--timetable',
                        dest='timetable',
                        action='store_true',
                        help='show full timetable instead of the next train')

    action.add_argument('-p', '--printer',
                        dest='printer',
                        choices=['table', 'text'],
                        default='text',
                        help='how to print the info (default: text)')

    return pparser


def main():
    'Main func'
    parser = create_parser()
    args = parser.parse_args()
    rr = RenfeRoute(args.origin, args.destine)

    try:
        if args.timetable:
            trains = rr.timetable()
        else:
            trains = rr.nextTrain()
    except ValueError as e:
        print(e)
        sys.exit(-1)

    if args.printer == 'table' or args.timetable:
        TimetablePrinter.as_table(trains)
    else:
        TimetablePrinter.as_text(trains)


if __name__ == '__main__':
    main()

# vim: ai ts=4 sts=4 et sw=4
