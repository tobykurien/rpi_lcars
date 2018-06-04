import errno
import socket


def local_ip_address():
    """
    Returns the IP address of the machine we're running on.

    If the test socket cannot connect for any reason, returns a string that
    attempts to describe the problem (sort of). At the moment, a machine that
    is connected to a LAN that doesn't have a route to the internet will return
    'LOCAL ONLY'; a different method of obtaining the IP address will probably
    be needed in those instances.

    In the future this function should possibly be converted to a service that
    automatically updates if the status of the network changes, but that would
    obviously be a large overhaul of the entire system (basically switching
    widgets to a publish/subscribe model).
    """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        result = s.getsockname()[0]
    except IOError as e:
        result = errno_message(e.errno)

    return result


def errno_message(err):
    lookup = {
        100: 'OFFLINE',
        101: 'NO NETWORK',
        113: 'LOCAL ONLY'
    }
    return lookup.get(err, 'NET ERROR {0}'.format(err))
