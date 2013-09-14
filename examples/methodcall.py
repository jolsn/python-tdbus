#!/usr/bin/env python
#
# This file is part of python-tdbus. Python-tdbus is free software
# available under the terms of the MIT license. See the file "LICENSE" that
# was provided together with this source file for the licensing terms.
#
# Copyright (c) 2012 the python-tdbus authors. See the file "AUTHORS" for a
# complete list.

# This example shows how to handle a method call.

from tdbus import DBusHandler, method, SimpleDBusConnection, DBUS_BUS_SESSION


class MethodHandler(DBusHandler):

    @method(interface="com.example.Hello", path="/com/example/TDBus")
    def Hello(self, message):
        hello = 'Hello world!'
        print 'receive a Hello request, responding with "{}"'.format(hello)
        self.set_response('s', (hello,))



conn = SimpleDBusConnection(DBUS_BUS_SESSION)
handler = MethodHandler()
conn.add_handler(handler)

print 'Exposing a hello world method on the bus.'
print 'In another terminal, issue:'
print
print '  $ dbus-send --session --print-reply --dest={} /com/example/TDBus com.example.Hello.Hello'.format(conn.get_unique_name())
print
print 'Press CTRL-c to exit.'
print
conn.dispatch()
