#!/usr/bin/env python
#
# This file is part of python-tdbus. Python-tdbus is free software
# available under the terms of the MIT license. See the file "LICENSE" that
# was provided together with this source file for the licensing terms.
#
# Copyright (c) 2012 the python-tdbus authors. See the file "AUTHORS" for a
# complete list.

# This example shows how to handle a method call.

from __future__ import print_function, unicode_literals
from __future__ import division, absolute_import

from tdbus import DBusHandler, method, SimpleDBusConnection, DBUS_BUS_SESSION
import tdbus


class MethodHandler(DBusHandler):

    @method(interface="com.example.Hello", path="/com/example/TDBus", member="Hello")
    def hello(self, message):
        hello = 'Hello world!'
        print('receive a Hello request, responding with "{}"'.format(hello))
        self.set_response('s', (hello,))


    @method(interface=tdbus.DBUS_INTERFACE_INTROSPECTABLE)
    def Introspect(self, message):
        """Return DBus introspection data for debugging

        @see: http://dbus.freedesktop.org/doc/dbus-specification.html#introspection-format

        This method is not required to implement a dbus method. But it makes debugging a lot easier.
        This is used by tools as d-feet to lookup what methods and signals are available
        """

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<node name="/com/example/TDBus">
        <interface name="com.example.Hello">
                <method name="Hello">
                        <arg type="s" name="message" direction="in" />
                        <arg type="s" name="hello_world" direction="out" />
                </method>
        </interface>
</node>"""

        self.set_response("s", [xml])

EXAMPLE_NAME = "com.example.Hello"

conn = SimpleDBusConnection(DBUS_BUS_SESSION)
conn.register_name(EXAMPLE_NAME)
handler = MethodHandler()
conn.add_handler(handler)

print('Exposing a hello world method on the bus.')
print('In another terminal, issue:')
print()
print('  $ dbus-send --session --print-reply --type=method_call --dest={} /com/example/TDBus com.example.Hello.Hello'.format(conn.get_unique_name()))
print()
print('or')
print()
print('  $ dbus-send --session --print-reply --type=method_call --dest={} /com/example/TDBus com.example.Hello.Hello'.format(EXAMPLE_NAME))
print()
print('Press CTRL-c to exit.')
print()

conn.dispatch()
