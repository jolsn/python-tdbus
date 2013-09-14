#!/usr/bin/env python
#
# This file is part of python-tdbus. Python-tdbus is free software
# available under the terms of the MIT license. See the file "LICENSE" that
# was provided together with this source file for the licensing terms.
#
# Copyright (c) 2012 the python-tdbus authors. See the file "AUTHORS" for a
# complete list.


# This example shows how to do a blocking method call. We call the bus function
# ListNames to list all bus names.

from tdbus import DBUS_BUS_SESSION, SimpleDBusConnection

conn = SimpleDBusConnection(DBUS_BUS_SESSION)

print 'Listing all well-known services on the system bus:'
print

result = conn.call_method('/', 'ListNames', 'org.freedesktop.DBus',
                                destination='org.freedesktop.DBus')

for name in result.get_args()[0]:
    if not name.startswith(':'):
        print '  %s' % name
print
