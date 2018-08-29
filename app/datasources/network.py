import psutil
from functools import reduce


def get_ip_address_string():
    """
    Consolidates a list of IP addresses into a string, stripping out any blank
    entries as well as the local `127.0.0.1` entry.
    """

    try:
        return ' '.join(get_ip_addresses())
    except:
        return ''

def get_ip_addresses():
    """
    Returns all the IP addresses of the machine we're running on.
    Shamelessly derived from:
        https://stackoverflow.com/questions/270745/how-do-i-determine-all-of-my-ip-addresses-when-i-have-multiple-nics
    """

    ip_list = filter(
        lambda ip: ip is not None and ip != '127.0.0.1',
        [interface_to_ip(v) for v in psutil.net_if_addrs().values()])

    return ip_list


def interface_to_ip(interface):
    """
    Gets the IPv4 address from a `net_if_addrs` interface record.
    The record is passed as a `snic` `namedtuple`.
    This function locates the IPv4 one and returns it.
    """
    for record in interface:
        if record.family == 2:  # AF_INET
            return record.address

    return None

