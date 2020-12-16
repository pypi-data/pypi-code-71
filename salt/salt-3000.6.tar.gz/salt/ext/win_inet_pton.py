# -*- coding: utf-8 -*-
# This software released into the public domain. Anyone is free to copy,
# modify, publish, use, compile, sell, or distribute this software,
# either in source code form or as a compiled binary, for any purpose,
# commercial or non-commercial, and by any means.

from __future__ import absolute_import

import socket
import ctypes
import os
from salt._compat import ipaddress
import salt.ext.six as six


class sockaddr(ctypes.Structure):
    _fields_ = [("sa_family", ctypes.c_short),
                ("__pad1", ctypes.c_ushort),
                ("ipv4_addr", ctypes.c_byte * 4),
                ("ipv6_addr", ctypes.c_byte * 16),
                ("__pad2", ctypes.c_ulong)]

if hasattr(ctypes, 'windll'):
    WSAStringToAddressA = ctypes.windll.ws2_32.WSAStringToAddressA
    WSAAddressToStringA = ctypes.windll.ws2_32.WSAAddressToStringA
else:
    def not_windows(*args):
        raise SystemError(
            "Invalid platform. ctypes.windll must be available."
        )
    WSAStringToAddressA = not_windows
    WSAAddressToStringA = not_windows


def inet_pton(address_family, ip_string):
    # Verify IP Address
    # This will catch IP Addresses such as 10.1.2
    if address_family == socket.AF_INET:
        try:
            ipaddress.ip_address(six.text_type(ip_string))
        except ValueError:
            raise socket.error('illegal IP address string passed to inet_pton')
        return socket.inet_aton(ip_string)

    # Verify IP Address
    # The `WSAStringToAddressA` function handles notations used by Berkeley
    # software which includes 3 part IP Addresses such as `10.1.2`. That's why
    # the above check is needed to enforce more strict IP Address validation as
    # used by the `inet_pton` function in Unix.
    # See the following:
    # https://stackoverflow.com/a/29286098
    # Docs for the `inet_addr` function on MSDN
    # https://msdn.microsoft.com/en-us/library/windows/desktop/ms738563.aspx
    addr = sockaddr()
    addr.sa_family = address_family
    addr_size = ctypes.c_int(ctypes.sizeof(addr))

    if WSAStringToAddressA(
            ip_string.encode('ascii'),
            address_family,
            None,
            ctypes.byref(addr),
            ctypes.byref(addr_size)
    ) != 0:
        raise socket.error(ctypes.FormatError())

    if address_family == socket.AF_INET:
        return ctypes.string_at(addr.ipv4_addr, 4)
    if address_family == socket.AF_INET6:
        return ctypes.string_at(addr.ipv6_addr, 16)

    raise socket.error('unknown address family')


def inet_ntop(address_family, packed_ip):
    addr = sockaddr()
    addr.sa_family = address_family
    addr_size = ctypes.c_int(ctypes.sizeof(addr))
    ip_string = ctypes.create_string_buffer(128)
    ip_string_size = ctypes.c_int(ctypes.sizeof(ip_string))

    if address_family == socket.AF_INET:
        if len(packed_ip) != ctypes.sizeof(addr.ipv4_addr):
            raise socket.error('packed IP wrong length for inet_ntoa')
        ctypes.memmove(addr.ipv4_addr, packed_ip, 4)
    elif address_family == socket.AF_INET6:
        if len(packed_ip) != ctypes.sizeof(addr.ipv6_addr):
            raise socket.error('packed IP wrong length for inet_ntoa')
        ctypes.memmove(addr.ipv6_addr, packed_ip, 16)
    else:
        raise socket.error('unknown address family')

    if WSAAddressToStringA(
            ctypes.byref(addr),
            addr_size,
            None,
            ip_string,
            ctypes.byref(ip_string_size)
    ) != 0:
        raise socket.error(ctypes.FormatError())

    return ip_string[:ip_string_size.value - 1]

# Adding our two functions to the socket library
if os.name == 'nt':
    socket.inet_pton = inet_pton
    socket.inet_ntop = inet_ntop
