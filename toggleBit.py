"""
Task: Implement Utils.toggleBit(int n, int bitPos)
"""


def checkBit(i, bitPos):
    return i & (1 << bitPos)

def setBit(i, bitPos):
    return i | (1 << bitPos)

def clearBit(i, bitPos):
    return i & (~(1 << bitPos))

def toggleBit(i, bitPos):
    return i ^ (1 << bitPos)


# key idea is to move left (<<) integer 1 ( = 00000001) to a bitPos (e.g. << 3) so it becomes ( = 00001000)
# and then perform logical operations with it: ^ (xor), | (or), & (and), ~(not)
