import socket


def local_ip_address():
    "Returns the IP address of the machine we're running on."
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    return s.getsockname()[0]
