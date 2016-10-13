"""
Task: Implement: IPv4 string to int
"""


def ipv4_to_int(ip):
    lst = ip.split(".")
    return int(lst[0])*(2**24) + int(lst[1])*(2**16) + int(lst[2])*(2**8) + int(lst[3])

ip = '64.233.187.99'
print ipv4_to_int(ip)