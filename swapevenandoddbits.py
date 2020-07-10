def swap_bits(x):
    return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1

x = 10000000
print(swap_bits(x))