import socket

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Unknown"

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            service_name = get_service_name(port)
            open_ports.append((port, service_name))
    return open_ports


if __name__ == '__main__':
    host = '192.168.1.1' #Choose the IP address of the target you want to scan, in my case it's the IP address of the router.
    open_ports = scan_ports(host, 20, 25) # choose the range of ports to scan 
    print(f"Open ports on {host}: {open_ports}")