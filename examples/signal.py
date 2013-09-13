#!/usr/bin/env python
#
# This file is part of python-tdbus. Python-tdbus is free software
# available under the terms of the MIT license. See the file "LICENSE" that
# was provided together with this source file for the licensing terms.
#
# Copyright (c) 2012 the python-tdbus authors. See the file "AUTHORS" for a
# complete list.


# This example shows how to listen for signals. Here we listen for any signal
# but signal_handler() also accepts keyword arguments to only listen for
# specific signals.

import sys
import tdbus
from tdbus import DBusHandler, signal_handler, SimpleDBusConnection, DBUS_BUS_SESSION

class SignalHandler(DBusHandler):
    
    @signal_handler()
    def Signal(message):
         print 'signal received: %s, args = %s' % (message.get_member(), repr(message.get_args()))


conn = tdbus.SimpleDBusConnection(DBUS_BUS_SESSION)
handler = SignalHandler()
conn.add_handler(handler)

print 'Listening for signals. Press CTRL-c to quit.'
print

while True:
    pass
