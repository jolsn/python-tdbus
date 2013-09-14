#!/usr/bin/env python
#
# This file is part of python-tdbus. Python-tdbus is free software
# available under the terms of the MIT license. See the file "LICENSE" that
# was provided together with this source file for the licensing terms.
#
# Copyright (c) 2012 the python-tdbus authors. See the file "AUTHORS" for a
# complete list.


# This example shows how to listen for signals. Here we listen for any signal named "Hello" on interface 
# com.example.Hello but signal_handler() also accepts keyword arguments to only listen for
# specific signals.

import sys
import tdbus
from tdbus import GEventDBusConnection, DBUS_BUS_SESSION, signal_handler, DBusHandler
import gevent

if not hasattr(tdbus, 'GEventDBusConnection'):
    print 'gevent is not available on this system'
    sys.exit(1)


class GEventHandler(DBusHandler):

    @signal_handler(interface="com.example.Hello")
    def Hello(self, message):
        print 'signal received: %s, args = %s' % (message.get_member(), repr(message.get_args()))



conn = GEventDBusConnection(DBUS_BUS_SESSION)
handler = GEventHandler()
conn.add_handler(handler)

print 'Listening for signals, with gevent dispatcher.'
print 'In another terminal, issue:'
print
print '  $ dbus-send --session --type=signal --dest={} /com/example/TDBus com.example.Hello.Hello'.format(conn.get_unique_name())
print
print 'Press CTRL-c to exit.'
print


while True:
    gevent.sleep(1)

